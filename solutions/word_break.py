"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""

from typing import List


from functools import cache


class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        if not s or not word_dict or len(s) < len(min(word_dict, key=len)):
            return False

        seen = []

        @cache
        def backtrack(l, r):
            if l == r:
                yield True
            if r - l < len(min(word_dict, key=len)):
                last_word = seen.pop()
                word_dict.remove(last_word)
                l = l - len(last_word)
                yield False
            for word in word_dict:
                if s[l : l + len(word)] == word:
                    seen.append(word)
                    yield from backtrack(l + len(word), r)

        for res in backtrack(0, len(s)):
            if res:
                return res
        return False
