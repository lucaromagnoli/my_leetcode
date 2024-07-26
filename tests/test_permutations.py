import pytest
from solutions.permutations import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        (
            [1, 2, 3],
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        ),  # Example 1
        ([0, 1], [[0, 1], [1, 0]]),  # Example 2
        ([1], [[1]]),  # Example 3
        ([], []),  # Edge case: empty list
        (
            [-1, 0, 1],
            [
                [-1, 0, 1],
                [-1, 1, 0],
                [0, -1, 1],
                [0, 1, -1],
                [1, -1, 0],
                [1, 0, -1],
            ],
        ),  # Negative and positive numbers
    ],
)
def test_permutes_correctly(solution, nums, expected):
    result = solution.permute(nums)
    assert sorted(result) == sorted(expected)
