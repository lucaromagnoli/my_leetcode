import pytest
from solutions.jump_game import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 1, 1, 4], True),  # Example 1
        ([3, 2, 1, 0, 4], False),  # Example 2
        ([0], True),  # Single element
        ([2, 0, 0], True),  # Can jump over zeros
        ([1, 2, 3], True),  # Simple case
        ([1, 0, 1, 0], False),  # Stuck at zero
        ([2, 5, 0, 0], True),  # Can jump over multiple zeros
        ([1, 1, 1, 1, 1], True),  # All ones
        ([1, 1, 0, 1], False),  # Stuck at zero
        ([2, 3, 1, 1, 0, 0, 4], False),  # Stuck before the end
    ],
)
def test_reaches_last_index(solution, nums, expected):
    result = solution.canJump(nums)
    assert result == expected
