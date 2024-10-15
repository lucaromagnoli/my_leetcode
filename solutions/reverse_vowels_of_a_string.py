"""
https://leetcode.com/problems/reverse-vowels-of-a-string/
Title: Reverse Vowels of a String
No: 345
Difficulty: Easy
Category: Algorithms
Problem:
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
 
Example 1:

Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"
Output: "leotcede"

 
Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.


"""


class Solution:
    def reverseVowels(self, string: str) -> str:
        string = list(string)
        vowels_tuple = ("a", "e", "i", "o", "u")
        vowels = [c for c in string if c.lower() in vowels_tuple]
        reversed_vowels = vowels[::-1]
        vowels_idx = [i for i, c in enumerate(string) if c.lower() in vowels_tuple]
        for i, idx in enumerate(vowels_idx):
            string[idx] = reversed_vowels[i]
        return "".join(string)
