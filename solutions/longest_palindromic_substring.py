"""
Given a string s, return the longest
palindromic

substring
 in s.



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
        solutions = []
        i = 0
        while i < len(s):
            j = len(s)
            while j > i:
                if s[i:j] == s[i:j][::-1]:
                    solutions.append(s[i:j])
                    break
                else:
                    j -= 1
            i += 1

        return max(solutions, key=len)
