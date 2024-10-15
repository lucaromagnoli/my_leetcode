import pytest
from solutions.combination_sum_ii import Solution


@pytest.mark.parametrize(
    "candidates, target, expected",
    [
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
        ([1, 1, 1, 1], 2, [[1, 1]]),  # Multiple duplicates
        (
            [1, 2, 3, 4, 5],
            10,
            [[1, 2, 3, 4], [1, 4, 5], [2, 3, 5]],
        ),  # Multiple combinations
        ([1, 2], 4, []),  # No valid combinations
        ([1], 1, [[1]]),  # Single element equal to target
        ([1, 2, 3], 0, []),  # Target is zero
        ([1, 2, 3], 7, []),  # Target greater than sum of all elements
    ],
)
def test_combination_sum_various_cases(candidates, target, expected):
    solution = Solution()
    result = solution.combinationSum2(candidates, target)
    assert sorted(result) == sorted(expected)
