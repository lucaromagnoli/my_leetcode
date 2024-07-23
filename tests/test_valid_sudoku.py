import pytest
from solutions.valid_sudoku import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("board, expected", [
    ([["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]], True),  # Valid Sudoku
    ([["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]], False),  # Invalid Sudoku due to duplicate '8' in a sub-box
    ([[".",".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".",".","."]], True),  # Empty Sudoku
    ([["1","2","3","4","5","6","7","8","9"],
      ["2","3","4","5","6","7","8","9","1"],
      ["3","4","5","6","7","8","9","1","2"],
      ["4","5","6","7","8","9","1","2","3"],
      ["5","6","7","8","9","1","2","3","4"],
      ["6","7","8","9","1","2","3","4","5"],
      ["7","8","9","1","2","3","4","5","6"],
      ["8","9","1","2","3","4","5","6","7"],
      ["9","1","2","3","4","5","6","7","8"]], False),  # Invalid Sudoku due to incorrect rows
    ([[".",".",".",".",".",".","5",".","."],
      [".",".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".",".","."],
      ["9","3",".",".","2",".","4",".","."],
      [".",".","7",".",".",".","3",".","."],
      [".",".",".",".",".",".",".",".","."],
      [".",".",".","3","4",".",".",".","."],
      [".",".",".",".",".","3",".",".","."],
      [".",".",".",".",".","5","2",".","."]], False),  # Invalid Sudoku due to '5' appearing twice in a column
])
def test_valid_sudoku(solution, board, expected):
    assert solution.isValidSudoku(board) == expected