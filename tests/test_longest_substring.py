import pytest
from solutions.longest_substring import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("input_string, expected_length", [
    ("abcabcbb", 3),  # Example 1: no repeating characters
    ("bbbbb", 1),  # Example 2: all characters are the same
    ("pwwkew", 3),  # Example 3: mix of repeating and non-repeating characters
    ("", 0),  # Empty string
    (" ", 1),  # Single space
    ("au", 2),  # Two distinct characters
    ("dvdf", 3),  # Repeating character after a non-repeating sequence
    ("anviaj", 5),  # Long non-repeating sequence
    ("aabbccdd", 2),  # Repeating characters with no overlap
    ("tmmzuxt", 5),  # Complex case with multiple repeating characters
])
def test_length_of_longest_substring(solution, input_string, expected_length):
    assert solution.lengthOfLongestSubstring(input_string) == expected_length