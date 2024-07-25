import pytest
from solutions.three_sum_closest import Solution


@pytest.fixture
def solution():
    return Solution()


test_data = [
    ([-1, 2, 1, -4], 1, 2),  # Closest sum to target with negative and positive numbers
    ([0, 0, 0], 1, 0),  # All elements are the same and closest sum is the sum itself
    ([1, 1, 1, 0], -100, 2),  # Target is much smaller than any possible sum
    ([1, 2, 4, 8, 16, 32, 64, 128], 82, 82),  # Exact match for target
    ([-100, -98, -2, 0, 1, 5], 0, -1),  # Closest sum with mostly negative numbers
    ([34, 23, 1, 24, 75, 33, 54, 8], 60, 59),  # Random numbers with a specific target
    (
        [1, 2, 5, 10, 11],
        12,
        13,
    ),  # Closest sum requires skipping the closest individual number
    ([-1, -1, 1, 1, 3], 0, -1),  # Zero target with negative and positive numbers
]


@pytest.mark.parametrize("nums, target, expected", test_data)
def test_three_sum_closest(solution, nums, target, expected):
    assert solution.threeSumClosest(nums, target) == expected
