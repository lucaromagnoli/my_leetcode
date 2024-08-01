import pytest
from solutions.valid_palindrome import Solution

@pytest.mark.parametrize("s, expected", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
])
def test_is_palindrome_correctness(s, expected):
    solution = Solution()
    assert solution.isPalindrome(s) == expected

@pytest.mark.parametrize("s, expected", [
    ("", True),
    ("a", True),
    ("ab", False),
    ("aa", True),
    ("0P", False),
])
def test_is_palindrome_edge_cases(s, expected):
    solution = Solution()
    assert solution.isPalindrome(s) == expected