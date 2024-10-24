import pytest
from solutions.can_place_flowers import Solution


@pytest.mark.parametrize(
    "flowerbed, n, expected",
    [
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ([0, 0, 0, 0, 0], 3, True),  # All empty plots
        ([1, 0, 0, 0, 0, 1], 1, True),  # One flower can be placed in the middle
        ([1, 0, 0, 0, 0, 1], 2, False),  # Not enough space for two flowers
        ([0, 0, 1, 0, 0], 1, True),  # Flower can be placed at the start
        ([0, 0, 1, 0, 0], 2, True),  # Only one flower can be placed
        ([1, 0, 1, 0, 1, 0, 1], 1, False),  # No space for any flower
        ([0, 0, 0, 0, 1], 2, True),  # Two flowers can be placed at the start
        ([1, 0, 0, 0, 0], 2, True),  # Two flowers can be placed at the end
    ],
)
def test_can_place_flowers_various_cases(flowerbed, n, expected):
    solution = Solution()
    result = solution.canPlaceFlowers(flowerbed, n)
    assert result == expected
