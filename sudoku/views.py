from django.shortcuts import render, redirect
from sudoku.solver import Solver


def index(request):
    # Solve puzzle or redirect if there is GET parameters
    if request.GET:
        # Check if the get field is a valid sudoku puzzle
        valid = True
        values = dict()
        for l in "ABCDEFGHI":
            for n in "123456789":
                # Check that all squares are in the request
                if l+n not in request.GET:
                    valid = False
                else:
                    # If the key is in the get, check if the value is valid
                    if len(request.GET[l+n]) > 1:
                        valid = False
                    elif len(request.GET[l+n]) == 1:
                        if request.GET[l+n] not in "123456789":
                            # If there was an invalid character in the input
                            valid = False
                        else:
                            # Add the value to the values dictionary
                            values[l+n] = request.GET[l+n]
        if valid:
            print("Valid input, trying to solve")
            values = Solver(values).values
            if values:
                return render(request, 'sudoku/index.html', {'values': values})
        print("Invalid input, redirecting")
        return redirect('index')
    else:
        return render(request, 'sudoku/index.html')
