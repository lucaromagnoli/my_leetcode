"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words/
Title: Substring with Concatenation of All Words
No: 30
Difficulty: Hard
Category: Algorithms
Problem:
You are given a string s and an array of strings words. All the strings of words are of the same length.
A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.

Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.
 
Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation:
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation:
There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation:
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 
Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.


"""

from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, string: str, words: list[str]) -> list[int]:
        """
        :type string: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not string:
            return []

        word_counter = Counter(words)
        word_len = len(words[0])
        string_len = len(string)
        substr_len = len(words) * word_len
        results = []
        for left in range(string_len - substr_len + 1):
            seen = defaultdict(int)
            for right in range(left, left + substr_len, word_len):
                substring = string[right: right + word_len]
                if substring in word_counter:
                    seen[substring] += 1
                    if seen[substring] > word_counter[substring]:
                        break
                else:
                    break
            else:
                results.append(left)

        return results
