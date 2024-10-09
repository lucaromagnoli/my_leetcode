import pytest
from solutions.is_subsequence import Solution

@pytest.mark.parametrize("s, t, expected", [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
    ("", "ahbgdc", True),  # Empty s
    ("abc", "", False),  # Empty t
    ("", "", True),  # Both s and t are empty
    ("a", "a", True),  # Single character match
    ("a", "b", False),  # Single character no match
    ("ace", "abcde", True),  # Subsequence with non-consecutive characters
    ("aec", "abcde", False),  # Non-subsequence with non-consecutive characters
    ("abc", "abc", True),  # Exact match
    ("abc", "aabbcc", True),  # Subsequence with repeated characters in t
    ("abc", "acb", False),  # Characters in wrong order
    ("aaaaaa", "bbaaaa", False)
])
def test_is_subsequence_various_cases(s, t, expected):
    solution = Solution()
    result = solution.isSubsequence(s, t)
    assert result == expected
