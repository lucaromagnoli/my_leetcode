import pytest
from solutions.reverse_vowels_of_a_string import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("IceCreAm", "AceCreIm"),
        ("leetcode", "leotcede"),
        ("aA", "Aa"),  # Case sensitivity
        ("", ""),  # Empty string
        ("bcdfg", "bcdfg"),  # No vowels
        ("aeiou", "uoiea"),  # All vowels
        ("AEIOU", "UOIEA"),  # All uppercase vowels
        ("hello", "holle"),  # Mixed consonants and vowels
        ("racecar", "racecar"),  # Palindrome with vowels
        ("a.b,c!d", "a.b,c!d"),  # Special characters
    ],
)
def test_reverse_vowels_various_cases(s, expected):
    solution = Solution()
    result = solution.reverseVowels(s)
    assert result == expected
