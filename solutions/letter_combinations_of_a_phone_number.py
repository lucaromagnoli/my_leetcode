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


def lex_gen(bounds):
    elem = [0] * len(bounds)
    while True:
        yield elem
        i = 0
        while elem[i] == bounds[i] - 1:
            elem[i] = 0
            i += 1
            if i == len(bounds):
                return
        elem[i] += 1


def cart_product(lists):
    bounds = [len(lst) for lst in lists]
    for elem in lex_gen(bounds):
        yield [lists[i][elem[i]] for i in range(len(lists))]


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
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
        if digits:
            letter_groups = [digits_to_letters[d] for d in digits]
            combinations = sorted(list("".join(p) for p in cart_product(letter_groups)))
        return combinations
