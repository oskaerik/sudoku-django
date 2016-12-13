"""Contains the Solver class"""
import copy
import time
import os


def solved(values):
    """Checks if a sudoku puzzle is solved or unsolvable, returns -1 if unsolvable, 1 if solved and 0 if not solved"""
    for u in values:
        if len(values[u]) < 1:
            return -1
        elif len(values[u]) > 1:
            return 0
    return 1


def clear():
    if __name__ == "__main__":
        os.system('cls' if os.name == 'nt' else 'clear')


class Solver(object):
    """The Solver class handles solving of the sudoku puzzle"""

    def __init__(self, input):
        """Constructor, creates the collection of rows, columns, boxes and the values"""
        self.letters = "ABCDEFGHI"
        self.numbers = "123456789"

        # Create rows
        self.rows = dict()
        for l in self.letters:
            row = list()
            for n in self.numbers:
                row.append(l + n)
            for u in row:
                self.rows[u] = row

        # Create columns
        self.columns = dict()
        for n in self.numbers:
            column = list()
            for l in self.letters:
                column.append(l + n)
            for u in column:
                self.columns[u] = column

        # Create boxes
        self.boxes = dict()
        for r in range(0, 3):
            for c in range(0, 3):
                box = list()
                for l in range(0, 3):
                    for n in range(0, 3):
                        box.append(self.letters[l+3*r] + self.numbers[n+3*c])
                for u in box:
                    self.boxes[u] = box

        # Create values
        self.values = dict()
        for l in self.letters:
            for n in self.numbers:
                self.values[l + n] = "123456789"

        # Parse the input lines
        self.parse(input)

        # Solve the puzzle
        self.start_time = time.time()
        self.values = self.solve(self.values)

        if self.values:
            clear()
            self.paint(self.values)
            print("Solved in " + str(time.time() - self.start_time) + " seconds")
        else:
            print("The puzzle was not solvable")

    def parse(self, input):
        for key in input:
            # Abort if there are duplicate values as input in the same row, column or box
            if input[key] in "123456789":
                for u in self.rows[key]:
                    if u != key and u in input and input[u] == input[key]:
                        self.values = False
                        return
                for u in self.columns[key]:
                    if u != key and u in input and input[u] == input[key]:
                        self.values = False
                        return
                for u in self.boxes[key]:
                    if u != key and u in input and input[u] == input[key]:
                        self.values = False
                        return
            self.assign(self.values, key, input[key])

    def remove(self, values, key, value):
        """Removes a value from the list of possible values for a square"""
        # Do nothing if the value isn't there
        if value not in values[key]:
            return

        # Remove the value from the square
        values[key] = values[key].replace(value, "")

        # If the square only has one possible value, assign it
        if len(values[key]) == 1:
            self.assign(values, key, values[key])

        # Checks if there exists value that only can be in one place in the row, column or box
        for i in range(1, 10):
            self.single(values, self.rows, key, str(i))
            self.single(values, self.columns, key, str(i))
            self.single(values, self.boxes, key, str(i))

    def assign(self, values, key, value):
        """Assigns a value to a square"""
        # Do nothing if the value isn't there
        if value not in values[key]:
            return

        # Remove all other values from possible values
        remove = values[key].replace(value, "")
        for r in remove:
            self.remove(values, key, r)

        # Removes the value from the squares in the square's row, column and box
        for u in self.rows[key]:
            if not u == key:
                self.remove(values, u, value)
        for u in self.columns[key]:
            if not u == key:
                self.remove(values, u, value)
        for u in self.boxes[key]:
            if not u == key:
                self.remove(values, u, value)

    def single(self, values, group, key, value):
        """Checks if there is only a single place a value can fit"""
        candidates = list()
        for u in group[key]:
            if value in values[u]:
                candidates.append(u)
        # Check for a single place the value can fit
        if len(candidates) == 1 and len(values[candidates[0]]) > 1:
            self.assign(values, candidates[0], value)

    def paint(self, values):
        """Paints the grid in standard out"""
        for r, n in enumerate(self.numbers):
            if r % 3 == 0:
                print("-------------------------")
            print("|", end="")
            for c, l in enumerate(self.letters):
                if c % 3 == 0 and c != 0:
                    print(" |", end="")
                if len(values[l + n]) > 1:
                    print("  ", end="")
                elif len(values[l + n]) < 1:
                    print("  ", end="")
                else:
                    print(" " + values[l + n], end="")
            print(" |")
        print("-------------------------")

    def solve(self, mother):
        """Solves the puzzle recursively"""
        if not mother:
            return False
        if __name__ == "__main__":
            clear()
            self.paint(mother)
        # Checks for time out
        if (time.time() - self.start_time) > 120:
            print("Timed out")
            return False

        if solved(mother) == 1:
            # If the puzzle is solved, return true
            return mother
        elif solved(mother) == -1:
            # If the puzzle is unsolvable, return false
            return False

        # Find a square and a possible value
        find = self.find(mother)

        # Create a child and assign the possible value to the square
        child = copy.deepcopy(mother)
        self.assign(child, find[0], find[1])

        # Try to solve the child
        child = self.solve(child)
        if child:
            return child
        else:
            self.remove(mother, find[0], find[1])
            return self.solve(mother)

    def find(self, values):
        """Find a square with more than one possible value and return the first as tuple"""
        for l in self.letters:
            for n in self.numbers:
                if len(values[l + n]) > 1:
                    return l + n, values[l + n][0]


if __name__ == "__main__":
    print("Was main, solving")
    puzzle = "800000000003600000070090200050007000000045700000100030001000068008500010090000400"  # arto
    #puzzle = "600008940900006100070040000200610000000000200089002000000060005000000030800001600"  # wiki
    val = dict()
    let = "ABCDEFGHI"
    num = "123456789"
    # Add values to dict
    for n in range(0, 9):
        for l in range(0, 9):
            val[let[l] + num[n]] = puzzle[n * 9 + l]

    solver = Solver(val)

