import pytest
from solutions.two_sum import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),  # Example 1
    ([3, 2, 4], 6, [1, 2]),  # Example 2
    ([3, 3], 6, [0, 1]),  # Example 3
    ([1, 2, 3, 4, 5], 9, [3, 4]),  # General case
    ([0, 4, 3, 0], 0, [0, 3]),  # Zeroes in the list
    ([-3, 4, 3, 90], 0, [0, 2]),  # Negative numbers
    ([1, 1, 1, 1], 2, [0, 1]),  # Repeated numbers
    ([2, 5, 5, 11], 10, [1, 2]),  # Multiple pairs possible
])
def test_returns_correct_indices(solution, nums, target, expected):
    assert solution.twoSum(nums, target) == expected