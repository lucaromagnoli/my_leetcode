import pytest
from other.jump_game_ii import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 1, 1, 4], 2),  # Example 1
        ([2, 3, 0, 1, 4], 2),  # Example 2
        ([1, 2, 3], 2),  # Simple case
        ([1, 1, 1, 1], 3),  # All ones
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0], 2),  # Large first jump
        ([1, 2, 1, 1, 1], 3),  # Multiple small jumps
        ([1], 0),  # Single element
        ([0], 0),  # Single zero element
    ],
)
def test_returns_minimum_jumps(solution, nums, expected):
    assert solution.jump(nums) == expected
