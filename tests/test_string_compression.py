import pytest
from solutions.string_compression import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("chars, expected_length, expected_chars", [
    (["a","a","b","b","c","c","c"], 6, ["a","2","b","2","c","3"]),  # Example 1
    (["a"], 1, ["a"]),  # Example 2
    (["a","b","b","b","b","b","b","b","b","b","b","b","b"], 4, ["a","b","1", "2"]),  # Example 3
    (["a","a","a","a","a","a","a","a","a","a","a","a","a"], 3, ["a","1", "3"]),  # Long sequence of a single character
    (["a","b","c"], 3, ["a","b","c"]),  # No compression needed
    (["a","a","a","b","b","a","a"], 6, ["a","3","b","2","a","2"]),  # Mixed groups
    (["a","a","a","a","b","b","b","b","c","c","c","c"], 6, ["a","4","b","4","c","4"]),  # Multiple groups of same length
    (["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"], 3, ["a","2", "0"]),  # Group length > 9
    (["a","b","c","c","c","c","c","c","c","c","c","c","c"], 5, ["a","b","c","1", "1"]),  # Group length exactly 10
])
def test_compresses_correctly(solution, chars, expected_length, expected_chars):
    assert solution.compress(chars) == expected_length
    assert chars[:expected_length] == expected_chars