import pytest
from solutions.removing_stars_from_a_string import Solution

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("leet**cod*e", "lecoe"),  # Example 1
        ("erase*****", ""),  # Example 2
        ("a*b*c*", ""),  # All characters removed
        ("abc*de**f", "abf"),  # Multiple stars in sequence
        ("", ""),  # Empty string
        ("no*stars", "nstars"),  # No stars
        ("*a", "a"),  # Star at the beginning
        ("a*", ""),  # Star at the end
        ("a*b*c*d*e*f*", ""),  # Alternating characters and stars
        ("abc", "abc"),  # No stars, all characters remain
    ],
)
def test_removing_stars_from_string(input_string, expected_output):
    solution = Solution()
    assert solution.removeStars(input_string) == expected_output
