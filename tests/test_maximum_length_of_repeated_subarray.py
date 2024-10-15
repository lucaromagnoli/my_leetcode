import pytest
from solutions.maximum_length_of_repeated_subarray import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 9),
        ([1, 2, 3, 2, 1], [3, 2, 1, 4, 7], 3),  # Example 1
        ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 5),  # Example 2
        ([1, 2, 3], [4, 5, 6], 0),  # No common subarray
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 1),  # Single element match
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5),  # Identical arrays
        ([1, 2, 3, 4, 5], [2, 3, 4], 3),  # Subarray in the middle
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 0),  # Completely different arrays
        ([1, 2, 3, 2, 1], [1, 2, 3, 2, 1], 5),  # Repeated pattern
        ([1, 2, 3, 4, 5], [3, 4, 5, 6, 7], 3),  # Overlapping subarray
        ([1], [1], 1),  # Single element arrays
    ],
)
def test_returns_maximum_length_of_repeated_subarray(solution, nums1, nums2, expected):
    assert solution.findLength(nums1, nums2) == expected
