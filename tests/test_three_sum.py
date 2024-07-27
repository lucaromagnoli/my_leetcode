import json

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
    ][:],
)
def test_three_sum_finds_all_unique_triplets_that_sum_to_zero(
    solution, nums, expected_output
):
    result = sorted([sorted(r) for r in solution.threeSum(nums)])
    expected_output = sorted([sorted(r) for r in expected_output])
    assert (
            result == expected_output
    ), f"expected {expected_output} but got {result} for input {nums}"


@pytest.fixture
def large_input(shared_datadir):
    with open(shared_datadir / "three_sum1.json") as f:
        return json.load(f)

# def test_timeout(large_input, solution):
#     solution.threeSum(large_input)



