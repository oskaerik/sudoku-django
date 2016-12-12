var letters = "ABCDEFGHI".split("");
var numbers = "123456789".split("");

function clearPuzzle() {
  for (l = 0; l < 9; l++) {
    for (n = 0; n < 9; n++) {
      document.getElementById(letters[l] + numbers[n]).value = "";
    }
  }
}

function fillPuzzle(puzzle) {
  var preset = [];
  preset[0] = `Arto Inkala
800000000
003600000
070090200
050007000
000045700
000100030
001000068
008500010
090000400`;

  preset[1] = `SudokuWiki Unsolveable #26
600008940
900006100
070040000
200610000
000000200
089002000
000060005
000000030
800001600`
  clearPuzzle();
  sudoku = preset[puzzle].split("\n");
    for (r = 1; r < 10; r++) {
      var line = sudoku[r].split("");
      for (c = 0; c < 9; c++) {
        // If the number isn't a zero
        if (line[c] != "0") {
          var square = letters[c] + numbers[r-1];
          document.getElementById(square).value = line[c];
        }
      }
    }
}
