from functools import cache


class Solution:
    def can_be_placed(self, tboard, row_idx, col_idx, number):
        column = [tboard[r][col_idx] for r in range(9)]
        box_row = (row_idx // 3) * 3
        box_col = (col_idx // 3) * 3
        box = [tboard[r][c] for r in range(box_row, box_row + 3) for c in range(box_col, box_col + 3)]
        return (
                number not in tboard[row_idx] and
                number not in column and
                number not in box
        )

    def solveSudoku(self, board: list[list[str]]) -> None:
        def solve():
            nonlocal board
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in range(1, 10):
                            if self.can_be_placed(board, i, j, str(num)):
                                board[i][j] = str(num)
                                if solve():
                                    return True
                                board[i][j] = "."
                        return False
            return True
        solve()
