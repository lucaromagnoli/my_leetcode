import pytest
from solutions.maximum_number_of_vowels_in_a_substring_of_given_length import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("abciiidef", 3, 3),  # Example 1
        ("aeiou", 2, 2),  # Example 2
        ("leetcode", 3, 2),  # Example 3
        ("rhythms", 4, 0),  # No vowels
        ("a", 1, 1),  # Single character
        ("a" * 100000, 100000, 100000),  # All vowels, maximum length
        ("b" * 100000, 1, 0),  # All consonants, minimum k
        ("aeiouaeiou", 5, 5),  # Repeated vowels
        ("aeiobcdfgh", 4, 4),  # Mixed vowels and consonants
        ("", 1, 0),  # Empty string
    ],
)
def test_returns_maximum_vowels(solution, s, k, expected):
    assert solution.maxVowels(s, k) == expected
