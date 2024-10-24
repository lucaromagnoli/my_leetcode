"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Title: Longest Substring Without Repeating Characters
No: 3
Difficulty: Medium
Category: Algorithms
Problem:
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.



"""


class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        longest = 0
        seen_chars = []
        r = 0
        for l in range(len(string)):
            while r < len(string) and string[r] not in seen_chars:
                seen_chars.append(string[r])
                r += 1
            longest = max(longest, len(string[l:r]))
            seen_chars.pop(0)
        return longest
