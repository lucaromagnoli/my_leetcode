"""
https://leetcode.com/problems/group-anagrams/
Title: Group Anagrams
No: 49
Difficulty: Medium
Category: Algorithms
Problem:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]

 
Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


"""

import itertools
import string
from collections import Counter


class Solution(object):
    def groupAnagrams(self, words):
        groups = {}
        for word in words:
            key = tuple(sorted(word))
            groups.setdefault(key, [])
            groups[key].append(word)
        return [v for k, v in groups.items()]
