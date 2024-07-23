"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

class Solution:
    def isValid(self, characters: str) -> bool:
        stack = [characters[0]]
        i = 1
        while i < len(characters):
            current = characters[i]
            if not stack:
                stack.append(current)
            else:
                previous = stack.pop()
                if f"{previous}{current}" in ('()', '[]', '{}'):
                    pass
                elif (previous == '(' and current in (']', '}') or
                      previous == '[' and current in (')', '}') or
                      previous == '{' and current in (')', ']')):
                    return False
                else:
                    stack.append(previous)
                    stack.append(current)
            i += 1
        if stack:
            return False
        return True


sol = Solution()
r = sol.isValid("()")
print(r)
