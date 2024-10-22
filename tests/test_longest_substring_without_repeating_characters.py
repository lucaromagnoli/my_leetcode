import pytest
from solutions.longest_substring_without_repeating_characters import Solution


@pytest.mark.parametrize(
    "input_string, expected_length",
    [
        ("abcabcbb", 3),  # Example 1
        ("bbbbb", 1),  # Example 2
        ("pwwkew", 3),  # Example 3
        ("", 0),  # Empty string
        ("abcdef", 6),  # All unique characters
        ("aab", 2),  # Repeating characters at the start
        ("dvdf", 3),  # Repeating characters in the middle
        ("anviaj", 5),  # Repeating characters at the end
        ("a" * 1000, 1),  # Long string with all same characters
        ("abcdefghijklmnopqrstuvwxyz", 26),  # Long string with all unique characters
    ],
)
def test_length_of_longest_substring(input_string, expected_length):
    solution = Solution()
    assert solution.lengthOfLongestSubstring(input_string) == expected_length
