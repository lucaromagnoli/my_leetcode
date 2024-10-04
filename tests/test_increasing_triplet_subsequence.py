import pytest
from solutions.increasing_triplet_subsequence import Solution

@pytest.mark.parametrize("nums, expected", [
    # ([1, 2, 3, 4, 5], True),
    # ([5, 4, 3, 2, 1], False),
    ([2, 1, 5, 0, 4, 6], True),
    ([1, 1, 1, 1, 1], False),  # All elements are the same
    ([1, 2], False),  # Less than three elements
    ([1, 2, 3], True),  # Exactly three elements in increasing order
    ([2, 4, -2, -3], False),  # No increasing triplet
    ([5, 1, 5, 5, 2, 5, 4], True),  # Triplet exists with non-consecutive elements
    ([1, 5, 0, 4, 1, 3], True),  # Triplet exists with mixed values
    ([1, 2, 3, 1, 2, 1], True),  # Triplet exists with repeated values
])
def test_increasing_triplet_various_cases(nums, expected):
    solution = Solution()
    result = solution.increasingTriplet(nums)
    assert result == expected
