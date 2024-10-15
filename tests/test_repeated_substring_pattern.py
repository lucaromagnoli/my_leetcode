import pytest
from solutions.repeated_substring_pattern import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abab", True),
        ("aba", False),
        ("abcabcabcabc", True),
        ("", False),  # Test for empty string
        ("a", False),  # Test for single character
        ("aa", True),  # Test for two identical characters
        ("abac", False),  # Test for non-repeating pattern
        ("abcabcabc", True),  # Test for repeating pattern
    ],
)
def test_repeated_substring_pattern_test(s, expected):
    solution = Solution()
    result = solution.repeatedSubstringPattern(s)
    assert result == expected
