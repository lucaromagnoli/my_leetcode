import pytest
from solutions.three_sum import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected_output",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, 2, -1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([], []),
        ([0], []),
        ([-1, 0, 1], [[-1, 0, 1]]),
        ([1, 2, -2, -1], []),
        ([-1, -1, -1, 2], [[-1, -1, 2]]),
    ],
)
def test_three_sum_finds_all_unique_triplets_that_sum_to_zero(
    solution, nums, expected_output
):
    result = solution.threeSum(nums)
    assert result == expected_output, f"expected {expected_output} but got {result} for input {nums}"
