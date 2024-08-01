"""
https://leetcode.com/problems/lucky-numbers-in-a-matrix/
Title: Lucky Numbers in a Matrix
No: 1496
Difficulty: Easy
Category: Algorithms
Problem:
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
 
Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

 
Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 105.
All elements in the matrix are distinct.
"""


class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        def is_lucky(idx_i, idx_j):
            num = matrix[idx_i][idx_j]
            is_min_in_row = num == min(matrix[idx_i])
            is_max_in_cols = num == max(matrix[i][idx_j] for i in range(len(matrix)))
            return is_min_in_row and is_max_in_cols

        numbers = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if is_lucky(i, j):
                    numbers.append(matrix[i][j])
        return numbers
