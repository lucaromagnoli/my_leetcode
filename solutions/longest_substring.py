"""
Given a string s, find the length of the longest
substring
 without repeating characters.

 Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        def find_substring(idx, chars):
            substring = [chars[idx]]
            sub_idx = idx + 1
            while sub_idx < len(chars):
                if chars[sub_idx] not in substring:
                    substring.append(chars[sub_idx])
                    sub_idx += 1
                else:
                    break
            return substring

        str_tuple = tuple(s)
        if len(str_tuple) == 1:
            return 1
        substrings = []
        for i in range(len(str_tuple)):
            s = find_substring(i, str_tuple)
            if s is not None:
                substrings.append(s)
        if substrings:
            return len(max(substrings, key=len))
        return 0


sol = Solution()
s = "pwwkew"
r = sol.lengthOfLongestSubstring(s)
print(r)