import pytest
from solutions.remove_duplicates_from_sorted_array_ii import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("nums, expected_k, expected_nums", [
    ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
    ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]),
    ([1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4], 8, [1, 1, 2, 2, 3, 3, 4, 4]),
    ([1, 1, 1, 1, 1], 2, [1, 1]),
    ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5])
])
def test_removes_duplicates_correctly(solution, nums, expected_k, expected_nums):
    k = solution.removeDuplicates(nums)
    assert k == expected_k
    assert nums[:k] == expected_nums
