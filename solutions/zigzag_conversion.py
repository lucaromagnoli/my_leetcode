"""
https://leetcode.com/problems/zigzag-conversion/
Title: Zigzag Conversion
No: 6
Difficulty: Medium
Category: Algorithms
Problem:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

 
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

 
Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000



"""


class Solution:

    @staticmethod
    def insert_at_column(column, item, row: list):
        idx = column
        while idx >= len(row):
            if idx == len(row):
                row.append(item)
            else:
                row.append("")
        return row

    def get_column(self, chars, column, i, matrix, numRows, row):
        while row < numRows and i < len(chars):
            c = chars[i]
            matrix[row] = self.insert_at_column(column, c, matrix[row])
            row += 1
            i += 1
        return i, row

    def get_diagonal(self, chars, column, i, matrix, row):
        while row > 1 and i < len(chars):
            c = chars[i]
            row -= 1
            i += 1
            matrix[row].append(c)
            column += 1
        return column, i

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == numRows:
            return s
        matrix = [[] for _ in range(numRows)]
        chars = list(s)
        i = 0
        column = 0
        while i < len(chars):
            # vertical
            row = 0
            i, row = self.get_column(chars, column, i, matrix, numRows, row)

            # diagonal
            column += 1
            row -= 1
            column, i = self.get_diagonal(chars, column, i, matrix, row)

        return "".join("".join(m) for m in matrix)
