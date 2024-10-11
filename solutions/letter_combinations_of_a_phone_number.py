"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Title: Letter Combinations of a Phone Number
No: 17
Difficulty: Medium
Category: Algorithms
Problem:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        if not digits:
            return []

        digits_to_letters = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z"),
        }
        combinations = []

        def backtrack(index, sol):
            if index == len(digits):
                combinations.append("".join(sol))
                return

            digit = digits[index]
            for letter in digits_to_letters[digit]:
                sol.append(letter)
                backtrack(index + 1, sol)
                sol.pop()

        backtrack(0, [])
        return combinations
