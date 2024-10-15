import pytest
from solutions.summary_ranges import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),  # Example 1
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),  # Example 2
        ([], []),  # Empty array
        ([1], ["1"]),  # Single element
        ([1, 3, 5, 7], ["1", "3", "5", "7"]),  # No ranges
        ([1, 2, 3, 4, 5], ["1->5"]),  # Single range
        ([-3, -2, -1, 0, 1], ["-3->1"]),  # Negative to positive range
        ([0, 1, 2, 50, 51, 52], ["0->2", "50->52"]),  # Disjoint ranges
        (
            [1, 3, 4, 5, 7, 8, 10],
            ["1", "3->5", "7->8", "10"],
        ),  # Mixed single and ranges
    ],
)
def test_returns_correct_summary_ranges(solution, nums, expected):
    assert solution.summaryRanges(nums) == expected
