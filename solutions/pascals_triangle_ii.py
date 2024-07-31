"""
https://leetcode.com/problems/pascals-triangle-ii/
Title: Pascal's Triangle II
No: 119
Difficulty: Easy
Category: Algorithms
Problem:
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 
Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:
Input: rowIndex = 0
Output: [1]
Example 3:
Input: rowIndex = 1
Output: [1,1]

 
Constraints:

0 <= rowIndex <= 33

 
Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def inner(idx, previous):
            if idx == rowIndex + 1:
                return previous
            current = []
            for i in range(len(previous) + 1):
                if i in [0, idx]:
                    current.append(1)
                else:
                    current.append(previous[i-1] + previous[i])
            return inner(idx + 1, current)
        return inner(1, [1])


