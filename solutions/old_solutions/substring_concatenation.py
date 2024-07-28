"""
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

from typing import List


class Solution:
    def permutations(self, iterable):
        def inner(a, left, right):
            if left == right:
                yield "".join(a)
            else:
                for idx in range(left, right):
                    if left != idx:
                        a[left], a[idx] = a[idx], a[left]
                    yield from inner(a, left + 1, right)
                    if left != idx:
                        a[left], a[idx] = a[idx], a[left]  # backtrack

        yield from inner(iterable, 0, len(iterable))

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        solutions = []
        seen = set()
        for substring in self.permutations(words):
            if substring not in seen and substring in s:
                seen.add(substring)
                i = 0
                while i < len(s):
                    try:
                        idx = s.index(substring, i)
                    except Exception as e:
                        print(e)
                    if idx >= 0:
                        solutions.append(idx)
                        i += len(substring)

        return solutions


solution = Solution()
s = "foobarfoobar"
words = ["foo", "bar"]
r = solution.findSubstring(s, words)
print(r)
