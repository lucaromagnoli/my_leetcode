"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/
Title: Greatest Common Divisor of Strings
No: 1146
Difficulty: Easy
Category: Algorithms
Problem:
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
 
Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

 
Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.


"""


class Solution:
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        shortest = min(str1, str2, key=len)
        longest = str1 if shortest == str2 else str2
        i = len(shortest)
        while i > 0:
            long_mul, short_mul = len(longest) / i, len(shortest) / i
            long_mul_int, short_mul_int = int(long_mul), int(short_mul)
            if long_mul_int == long_mul and short_mul_int == short_mul:
                if (
                    shortest[:i] * short_mul_int == shortest
                    and shortest[:i] * long_mul_int == longest
                ):
                    return shortest[:i]
            i -= 1
        return ""
