import pytest
from solutions.remove_dupes_from_sorted import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("nums, expected_length, expected_nums", [
    ([1, 1, 2], 2, [1, 2]),  # Basic case with duplicates
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),  # Multiple duplicates
    ([1, 2, 3, 4], 4, [1, 2, 3, 4]),  # No duplicates
    ([], 0, []),  # Empty list
    ([1, 1, 1, 1, 1], 1, [1]),  # All elements are the same
    ([-1, 0, 0, 0, 1, 1], 3, [-1, 0, 1]),  # Negative numbers and duplicates
])
def test_remove_duplicates(solution, nums, expected_length, expected_nums):
    assert solution.removeDuplicates(nums) == expected_length
    assert nums[:expected_length] == expected_nums
