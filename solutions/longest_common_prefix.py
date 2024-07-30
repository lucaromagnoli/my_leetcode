"""
https://leetcode.com/problems/longest-common-prefix/
Title: Longest Common Prefix
No: 14
Difficulty: Easy
Category: Algorithms
Problem:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
 
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.



"""
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest = min(strs, key=len)
        prefix = ""
        for i in range(len(shortest)):
            letters = set(s[i] for s in strs)
            if len(letters) == 1:
                letter = letters.pop()
                prefix = f"{prefix}{letter}"
            else:
                return prefix
        return prefix
