"""
https://leetcode.com/problems/reverse-integer/
Title: Reverse Integer
No: 7
Difficulty: Medium
Category: Algorithms
Problem:
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
        x = abs(x)
        result = int("".join(reversed(str(x))))
        if result < 2**31:
            if negative:
                return -result
            else:
                return result
        else:
            return 0
