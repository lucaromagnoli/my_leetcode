import pytest
from other.minimum_size_subarray_sum import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "target, nums, expected",
    [
        (7, [2, 3, 1, 2, 4, 3], 2),  # Example 1
        (4, [1, 4, 4], 1),  # Example 2
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),  # Example 3
        (15, [1, 2, 3, 4, 5], 5),  # Sum of all elements
        (100, [1, 2, 3, 4, 5], 0),  # Target not reachable
        (5, [5], 1),  # Single element equal to target
        (5, [1, 2, 3, 4, 5], 1),  # Single element in array
        (6, [1, 2, 3, 4, 5], 2),  # Subarray in the middle
        (3, [1, 1, 1, 1, 1], 3),  # Multiple elements equal to target
        (8, [2, 3, 1, 2, 4, 3], 3),  # Subarray at the end
    ],
)
def test_returns_minimal_length_subarray(solution, target, nums, expected):
    assert solution.minSubArrayLen(target, nums) == expected
