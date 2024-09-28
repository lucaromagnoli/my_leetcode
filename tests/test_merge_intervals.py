import pytest
from solutions.merge_intervals import Solution


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        (
            [[1, 4], [0, 4]],
            [[0, 4]],
        ),  # Test for intervals that start before the first interval
        (
            [[1, 4], [2, 3]],
            [[1, 4]],
        ),  # Test for intervals completely inside another interval
        ([[1, 4], [5, 6]], [[1, 4], [5, 6]]),  # Test for non-overlapping intervals
        ([[1, 4]], [[1, 4]]),  # Test for single interval
        ([[1, 4], [0, 0]], [[0, 0], [1, 4]]),  # Test for interval with zero length
    ],
)
def test_merge_intervals_various_cases_test(intervals, expected):
    solution = Solution()
    result = solution.merge(intervals)
    assert result == expected
