import pytest
from solutions.maximum_average_subarray_i import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("nums, k, expected", [
    ([1, 12, -5, -6, 50, 3], 4, 12.75),  # Example 1
    ([5], 1, 5.0),  # Example 2
    ([0, 4, 0, 3, 2], 1, 4.0),  # Single element max
    ([1, 1, 1, 1, 1], 5, 1.0),  # All elements same
    ([1, 2, 3, 4, 5], 2, 4.5),  # Increasing sequence
    ([-1, -2, -3, -4, -5], 2, -1.5),  # Decreasing sequence
])
def test_returns_maximum_average(solution, nums, k, expected):
    assert solution.findMaxAverage(nums, k) == expected