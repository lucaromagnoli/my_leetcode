"""Palindrome : Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def is_palindrome(string):
            if len(string) == 1:
                return True
            left_idx = 0
            right_idx = len(string) - 1
            while True:
                if string[left_idx] != string[right_idx]:
                    return False

                left_idx += 1
                right_idx -= 1
                if left_idx >= right_idx:
                    return True

        if len(s) == 1:
            return s
        if len(set(s)) == 1:
            return s
        char_len = {u: s.count(u) for u in set(s)}
        palindromes = []
        for i in range(len(s)):
            for j in reversed(range(i, len(s))):
                if is_palindrome(s[i : j + 1]):
                    palindromes.append(s[i : j + 1])

        return max(palindromes, key=len)
