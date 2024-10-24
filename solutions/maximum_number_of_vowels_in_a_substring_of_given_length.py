"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
Title: Maximum Number of Vowels in a Substring of Given Length
No: 1567
Difficulty: Medium
Category: Algorithms
Problem:
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
 
Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

 
Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length


"""


class Solution:
    def maxVowels(self, string: str, k: int) -> int:
        vowels = ("a", "e", "i", "o", "u")
        current_vowels = 0
        substring = string[:k]
        for s in substring:
            if s in vowels:
                current_vowels += 1
        max_vowels = current_vowels
        for i in range(1, len(string) - k + 1):
            if string[i - 1] in vowels:
                current_vowels -= 1

            if string[i + k - 1] in vowels:
                current_vowels += 1

            max_vowels = max(max_vowels, current_vowels)

        return max_vowels
