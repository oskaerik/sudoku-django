#sudoku-django
##An in-browser sudoku solver written in Python using Django

The solver is uploaded on: http://oskaerik.pythonanywhere.com/

If you want to run the solver locally:

* Clone the repository
* Install Django
* Run ```python manage.py runserver``` from a terminal in the root folder
* Go to http://localhost:8000/ in your browser

If you enter an invalid grid, it will try to find a solution for 120 seconds or until a contradiction was reached. The solver can find solutions for grids with more than one possible solution as long as it doesn't time out.

Happy solving!
