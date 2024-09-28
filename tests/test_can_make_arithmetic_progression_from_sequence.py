import pytest
from solutions.can_make_arithmetic_progression_from_sequence import Solution

@pytest.mark.parametrize("arr, expected", [
    ([3, 5, 1], True),
    ([1, 2, 4], False),
    ([1, 3, 5, 7], True),  # Already in arithmetic progression
    ([7, 5, 3, 1], True),  # Descending order arithmetic progression
    ([1, 1, 1, 1], True),  # All elements are the same
    ([1, 2, 3, 5], False),  # Missing element to form progression
    ([10, 0, -10, -20], True),  # Negative numbers in arithmetic progression
    ([1, 1000000], True),  # Only two elements
    ([1, 2, 2, 3], False),  # Duplicate elements breaking progression
])
def test_can_make_arithmetic_progression_various_cases(arr, expected):
    solution = Solution()
    result = solution.canMakeArithmeticProgression(arr)
    assert result == expected
