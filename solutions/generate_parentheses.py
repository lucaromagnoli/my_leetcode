"""
https://leetcode.com/problems/generate-parentheses/
Title: Generate Parentheses
No: 22
Difficulty: Medium
Category: Algorithms
Problem:
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


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        :type n: int
        :rtype: List[str]
        """
        solutions = []

        def backtrack(op, cl, sol):
            if len(sol) == n * 2:
                solutions.append("".join(sol))
                return

            if op < n:
                sol.append("(")
                backtrack(op + 1, cl, sol)
                sol.pop()

            if op > cl:
                sol.append(")")
                backtrack(op, cl + 1, sol)
                sol.pop()

        backtrack(0, 0, [])
        return solutions
