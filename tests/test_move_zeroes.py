import pytest
from solutions.move_zeroes import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1, 2, 3], [1, 2, 3]),  # No zeroes
        ([0, 0, 1], [1, 0, 0]),  # Multiple zeroes at the start
        ([1, 0, 0], [1, 0, 0]),  # Multiple zeroes at the end
        ([0, 1, 0, 0, 2, 3], [1, 2, 3, 0, 0, 0]),  # Mixed zeroes and non-zeroes
        ([0, 0, 0], [0, 0, 0]),  # All zeroes
        ([1], [1]),  # Single non-zero element
    ],
)
def test_move_zeroes_various_cases(nums, expected):
    solution = Solution()
    solution.moveZeroes(nums)
    assert nums == expected
