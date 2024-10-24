import pytest
from solutions.two_sum_ii_input_array_is_sorted import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([-1, 0], -1, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
        ([-3, -2, -1, 0, 1, 2, 3], 0, [1, 7]),
    ],
)
def test_returns_correct_indices(solution, numbers, target, expected):
    assert solution.twoSum(numbers, target) == expected
