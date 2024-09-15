"""
https://leetcode.com/problems/word-pattern/
Title: Word Pattern
No: 290
Difficulty: Easy
Category: Algorithms
Problem:
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
 
Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

 
Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.


"""


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        tokens = s.split()
        found = {}
        if len(tokens) != len(pattern):
            return False
        for i, p in enumerate(pattern):
            if pattern[i] in found and found[pattern[i]] != tokens[i]:
                return False
            found[pattern[i]] = tokens[i]
        return len(set(found.values())) == len(found.values())
