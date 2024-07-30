import pytest
from solutions.four_sum import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        (
            [1, 0, -1, 0, -2, 2],
            0,
            [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
        ),  # Example 1
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),  # Example 2
        ([1, 1, 1, 1], 4, [[1, 1, 1, 1]]),  # All elements the same
        ([1, 2, 3, 4, 5], 10, [[1, 2, 3, 4]]),  # Simple case
        ([], 0, []),  # Edge case: empty list
        ([1, 2, 3], 6, []),  # Not enough elements
        (
            [1, 0, -1, 0, -2, 2],
            1,
            [[-2, 0, 1, 2], [-1, 0, 0, 2]],
        ),  # Mixed positive and negative numbers
    ],
)
def test_finds_correct_quadruplets(solution, nums, target, expected):
    result = solution.fourSum(nums, target)
    assert sorted([sorted(quad) for quad in result]) == sorted(
        [sorted(quad) for quad in expected]
    )
