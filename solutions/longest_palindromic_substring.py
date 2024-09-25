"""
https://leetcode.com/problems/longest-palindromic-substring/
Title: Longest Palindromic Substring
No: 5
Difficulty: Medium
Category: Algorithms
Problem:
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.



"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        i = 0
        solution, max_len = None, 0
        while i < len(s) and i < len(s) - max_len:
            j = len(s)
            while j > i:
                if s[i:j] == s[i:j][::-1]:
                    if max_len is None or len(s[i:j]) > max_len:
                        max_len = len(s[i:j])
                        solution = s[i:j]
                    break
                else:
                    j -= 1
            i += 1

        return solution
