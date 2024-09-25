"""
https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
Title: Substrings of Size Three with Distinct Characters
No: 1987
Difficulty: Easy
Category: Algorithms
Problem:
A string is good if there are no repeated characters.
Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
A substring is a contiguous sequence of characters in a string.

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
The only good substring of length 3 is "xyz".

Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".


Constraints:

1 <= s.length <= 100
s​​​​​​ consists of lowercase English letters.


"""


class Solution:
    def countGoodSubstrings(self, string: str) -> int:
        counter = 0
        for i in range(len(string) - 2):
            if len(string[i : i + 3]) == len(set(string[i : i + 3])):
                counter += 1
        return counter
