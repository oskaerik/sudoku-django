#sudoku-django
##An in-browser sudoku solver written in Python using Django

The solver is uploaded on: http://oskaerik.pythonanywhere.com/

Or clone the repository, install django and run ```python manage.py runserver``` in the root folder and go to http://localhost:8000/ in your browser.

If you enter an invalid grid, it will try to find a solution for 120 seconds or until a contradiction was reached. The solver can find solutions for grids without a single possible solution as long as it doesn't time out.

Happy solving!
