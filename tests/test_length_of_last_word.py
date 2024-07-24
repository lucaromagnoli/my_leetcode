import pytest
from solutions.lenght_of_last_word import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("input_string, expected_length", [
    ("Hello World", 5),  # Standard case with a single space
    ("   fly me   to   the moon  ", 4),  # Multiple spaces around and within
    ("luffy is still joyboy", 6),  # No trailing spaces
    (" singleword ", 10),  # Single word with spaces around
    ("", 0),  # Empty string
    ("    ", 0),  # String with only spaces
    ("a ", 1),  # Single character word with trailing space
    ("a"*1000, 1000),  # Very long single word
    ("one two three " + "a"*1000, 1000),  # Long last word with preceding words
])
def test_length_of_last_word(solution, input_string, expected_length):
    assert solution.lengthOfLastWord(input_string) == expected_length