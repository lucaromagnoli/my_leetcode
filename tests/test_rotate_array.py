import pytest
from solutions.rotate_array import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),  # Example 1
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),  # Example 2
        ([1, 2, 3, 4, 5, 6, 7], 0, [1, 2, 3, 4, 5, 6, 7]),  # No rotation
        ([1, 2, 3, 4, 5, 6, 7], 7, [1, 2, 3, 4, 5, 6, 7]),  # Full rotation
        ([1, 2, 3, 4, 5, 6, 7], 10, [5, 6, 7, 1, 2, 3, 4]),  # k greater than length
        ([1], 1, [1]),  # Single element
        ([1, 2], 1, [2, 1]),  # Two elements
        ([1, 2, 3], 4, [3, 1, 2]),  # k greater than length by 1
    ],
)
def test_rotates_array_correctly(solution, nums, k, expected):
    solution.rotate(nums, k)
    assert nums == expected
