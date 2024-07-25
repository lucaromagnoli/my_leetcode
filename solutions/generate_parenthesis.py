"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""

from typing import List

import itertools

import itertools


class Solution:
    def is_valid_sequence(self, sequence):
        stack = []
        for current in sequence:
            if not stack:
                if current == ")":
                    return False
                else:
                    stack = [sequence[0]]
            else:
                previous = stack.pop()

                if f"{previous}{current}" == "()":
                    continue
                else:
                    stack.append(previous)
                    stack.append(current)
        # if stack is empty return True otherwise False
        return not stack

    def generateParenthesis(self, n: int) -> List[str]:

        results = []

        def dfs(open_p, closed_p, string):
            if open_p == closed_p and open_p + closed_p == n * 2:
                results.append(string)
                return

            if open_p < n:
                dfs(open_p + 1, closed_p, string + "(")

            if closed_p < open_p:
                dfs(open_p, closed_p + 1, string + ")")

        if n:
            dfs(0, 0, "")
        return results


Solution().generateParenthesis(3)
