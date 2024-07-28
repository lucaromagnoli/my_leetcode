"""
https://leetcode.com/problems/n-queens/
Title: N-Queens
No: 51
Difficulty: Hard
Category: Algorithms
Problem:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
 
Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

Input: n = 1
Output: [["Q"]]

 
Constraints:

1 <= n <= 9
"""
class Solution:
    def is_safe(self, board, row, col, n):
        # Check this row on the left side
        for i in range(col):
            if board[row][i] == 'Q':
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True

    def solveNQueens(self, n):
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []

        def backtrack(col):
            if col == n:
                result.append([''.join(row) for row in board])
                return

            for row in range(n):
                if self.is_safe(board, row, col, n):
                    board[row][col] = 'Q'
                    backtrack(col + 1)
                    board[row][col] = '.'

        backtrack(0)
        return result