"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""
from typing import List


class Solution:

    def traverse_rows(self, board):
        for row in board:
            yield row

    def traverse_columns(self, board):
        for column in zip(*board):
            yield column

    def traverse_quadrants(self, board):
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                quadrant = [board[r][col:col + 3] for r in range(row, row + 3)]
                yield [i for q in quadrant for i in q]

    def is_valid(self, symbols):
        numbers = [int(s) for s in symbols if s.isnumeric()]
        if numbers:
            has_unique_numbers = len(numbers) == len(set(numbers))
            is_right_range = 1 <= min(numbers) and max(numbers) <= 9
            return has_unique_numbers and is_right_range
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        has_valid_rows = all([self.is_valid(row) for row in self.traverse_rows(board)])
        has_valid_columns = all([self.is_valid(column) for column in self.traverse_columns(board)])
        has_valid_quadrants = all([self.is_valid(quadrant) for quadrant in self.traverse_quadrants(board)])
        return has_valid_rows and has_valid_columns and has_valid_quadrants


board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


s = Solution()
print(s.isValidSudoku(board))

