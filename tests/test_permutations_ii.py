import pytest
from solutions.permutations_ii import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),  # Example 1
        (
            [1, 2, 3],
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        ),  # Example 2
        ([1], [[1]]),  # Single element
        ([1, 1], [[1, 1]]),  # Duplicate elements
        ([1, 2, 2], [[1, 2, 2], [2, 1, 2], [2, 2, 1]]),  # Mixed duplicates
        ([], [[]]),  # Empty list
    ],
)
def test_returns_unique_permutations(solution, nums, expected):
    assert sorted(solution.permuteUnique(nums)) == sorted(expected)
