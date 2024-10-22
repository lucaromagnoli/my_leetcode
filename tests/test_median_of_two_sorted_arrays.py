import pytest
from solutions.median_of_two_sorted_arrays import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 3], [2], 2.0),  # Example 1
        ([1, 2], [3, 4], 2.5),  # Example 2
        ([], [1], 1.0),  # Single element in one array
        ([2], [], 2.0),  # Single element in the other array
        ([1, 2], [1, 2, 3], 2.0),  # Overlapping elements
        ([1, 3, 5], [2, 4, 6], 3.5),  # Interleaved elements
        ([1, 2, 3], [4, 5, 6], 3.5),  # Sequential elements
        ([1, 2, 3, 4], [5, 6, 7, 8], 4.5),  # Larger arrays
        # ([1, 3], [2, 7], 2.5),  # Different sized arrays
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5.5),  # Larger sequential arrays
    ],
)
def test_returns_median_of_two_sorted_arrays(solution, nums1, nums2, expected):
    assert solution.findMedianSortedArrays(nums1, nums2) == expected
