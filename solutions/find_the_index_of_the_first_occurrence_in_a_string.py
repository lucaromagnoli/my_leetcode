"""
https://leetcode.com/problems/implement-strstr/
Title: Implement strStr()
No: 28
Difficulty: Easy
Category: Algorithms
Problem:
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
 
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

 
Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.


"""


class Solution:
    def is_substring(self, idx, haystack, needle):
        i = 0
        while i < len(needle):
            if haystack[idx:][i] != needle[i]:
                return False
            i += 1
        return True

    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if needle[0] == haystack[i] and len(haystack) - i >= len(needle):
                if self.is_substring(i, haystack, needle):
                    return i
        return -1
