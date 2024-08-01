"""
https://leetcode.com/problems/sqrtx/
Title: Sqrt(x)
No: 69
Difficulty: Easy
Category: Algorithms
Problem:
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

 
Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

 
Constraints:

0 <= x <= 231 - 1


"""


class Solution:
    def mySqrt(self, num: int) -> int:

        def inner(previous, current):
            nonlocal num

            if current * current == num:
                return current
            elif previous * previous < num < current * current:
                return previous
            else:
                return inner(previous + 1, current + 1)

        if num in [0, 1]:
            return num
        return inner(1, 2)
