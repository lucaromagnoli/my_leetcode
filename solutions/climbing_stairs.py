"""
https://leetcode.com/problems/climbing-stairs/
Title: Climbing Stairs
No: 70
Difficulty: Easy
Category: Algorithms
Problem:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

 
Constraints:

1 <= n <= 45
"""

from functools import cache


class Solution:
    def climbStairs(self, steps: int) -> int:

        @cache
        def climb(n):
            if n in [0, 1]:
                return 1
            return climb(n - 1) + climb(n - 2)

        return climb(steps)
