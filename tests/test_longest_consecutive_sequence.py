import pytest
from solutions.longest_consecutive_sequence import Solution

@pytest.mark.parametrize("nums, expected", [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ([], 0),  # Test for empty array
    ([1, 2, 0, 1], 3),  # Test for duplicates
    ([1], 1),  # Test for single element
    ([1, 3, 5, 2, 4], 5),  # Test for all elements consecutive
    ([10, 5, 12, 3, 55, 30, 4, 11, 2], 4),  # Test for mixed elements
    ([-1, -2, -3, -4, -5], 5),  # Test for negative numbers
    ([1, 2, 0, 1, -1, -2, -3], 6),  # Test for mixed positive and negative numbers
])
def test_longest_consecutive_various_cases(nums, expected):
    solution = Solution()
    result = solution.longestConsecutive(nums)
    assert result == expected