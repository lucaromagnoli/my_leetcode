"""
https://leetcode.com/problems/repeated-substring-pattern/
Title: Repeated Substring Pattern
No: 459
Difficulty: Easy
Category: Algorithms
Problem:
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
 
Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:

Input: s = "aba"
Output: false

Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

 
Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.


"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        end = len(s) // 2
        while end > 0:
            mul = len(s) // len(s[:end])
            if s[:end] * mul == s:
                return True
            else:
                end -= 1
        return False