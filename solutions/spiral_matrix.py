"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 20
"""

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[""] * n for _ in range(n)]
        directions = ["right", "down", "left", "up"]
        d_idx = 0
        direction = directions[d_idx]
        for n_idx in range(0, n * n, n):
            numbers = list(range(n_idx, n_idx + n))
            self.fill_direction(matrix, numbers, direction)
