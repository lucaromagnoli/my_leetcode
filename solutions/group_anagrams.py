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
from collections import Counter


class Solution(object):

    def is_anagram(self, this_word, that_word):
        return Counter(this_word) == Counter(that_word)

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = []
        seen = set()
        for i in range(len(strs)):
            group = []
            if i not in seen:
                group = [strs[i]]
                seen.add(i)
                for j in range(i + 1, len(strs)):
                    if j not in seen:
                        if self.is_anagram(strs[i], strs[j]):
                            group.append(strs[j])
                            seen.add(j)
            if group:
                anagrams.append(group)
        return anagrams
