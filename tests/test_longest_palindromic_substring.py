import pytest
from solutions.longest_palindromic_substring import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("babad", "bab"),  # or "aba" as both are correct
        ("cbbd", "bb"),
        ("a", "a"),  # single character string
        ("ac", "a"),  # no palindrome longer than 1 character
        ("racecar", "racecar"),  # entire string is a palindrome
        ("", ""),  # empty string
        ("abb", "bb"),  # palindrome at the end
        ("aabba", "abba"),  # palindrome in the middle
    ],
)
def test_longest_palindrome(solution, input_string, expected_output):
    assert solution.longestPalindrome(input_string) == expected_output
