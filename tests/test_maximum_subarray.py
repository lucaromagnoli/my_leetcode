import pytest
from solutions.maximum_subarray import Solution

@pytest.mark.parametrize("nums, expected", [
    ([1, -3, 2, 1, -1], 3),
    ([5, 4, -1, 7, 8], 23),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([-1, -2, -3, -4], -1),
])
def test_maximum_subarray_correctness(nums, expected):
    solution = Solution()
    result = solution.maxSubArray(nums)
    assert result == expected

@pytest.mark.parametrize("nums, expected", [
    ([], 0),
    ([0, 0, 0, 0], 0),
    ([1, 2, 3, 4, 5], 15),
    ([-1, 0, 1], 1),
    ([2, -1, 2, -1, 2], 4),
])
def test_maximum_subarray_edge_cases(nums, expected):
    solution = Solution()
    result = solution.maxSubArray(nums)
    assert result == expected