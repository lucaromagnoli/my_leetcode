import pytest
from solutions.merge_sorted_array import Solution

@pytest.mark.parametrize("nums1, m, nums2, n, expected", [
    ([1, 2, 3, 0, 0, 0], 6, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([4,5,6,0,0,0], 3, [1,2,3], 3, [1,2,3,4,5,6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
    ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
    ([2, 0], 1, [1], 1, [1, 2]),
])
def test_merge_sorted_array_correctness(nums1, m, nums2, n, expected):
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    assert nums1 == expected

@pytest.mark.parametrize("nums1, m, nums2, n, expected", [
    ([0, 0, 0], 0, [1, 2, 3], 3, [1, 2, 3]),
    ([1, 2, 3], 3, [], 0, [1, 2, 3]),
    ([0, 0, 0], 0, [0, 0, 0], 3, [0, 0, 0]),
    ([1, 0, 0, 0], 1, [2, 3, 4], 3, [1, 2, 3, 4]),
])
def test_merge_sorted_array_edge_cases(nums1, m, nums2, n, expected):
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    assert nums1 == expected