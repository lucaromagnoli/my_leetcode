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
        if not n:
            return []
        parenthesis = "()" * n
        results = [parenthesis]
        for product in itertools.combinations(parenthesis, len(parenthesis)):
            results.append("".join(product))
        return results


