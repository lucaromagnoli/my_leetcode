"""
https://leetcode.com/problems/excel-sheet-column-number/
Title: Excel Sheet Column Number
No: 171
Difficulty: Easy
Category: Algorithms
Problem:
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnTitle = "A"
Output: 1

Example 2:

Input: columnTitle = "AB"
Output: 28

Example 3:

Input: columnTitle = "ZY"
Output: 701


Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].


"""

import string


class Solution:
    def titleToNumber(self, column: str) -> int:
        number = 0
        for i, c in enumerate(column[::-1]):
            number += (string.ascii_uppercase.index(c) + 1) * len(
                string.ascii_uppercase
            ) ** i
        return number
