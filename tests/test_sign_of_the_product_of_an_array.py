import pytest
from solutions.sign_of_the_product_of_an_array import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, -2, -3, -4, 3, 2, 1], 1),
        ([1, 5, 0, 2, -3], 0),
        ([-1, 1, -1, 1, -1], -1),
        ([1, 2, 3, 4, 5], 1),  # All positive numbers
        ([-1, -2, -3, -4, -5], -1),  # All negative numbers
        ([0, 0, 0], 0),  # All zeroes
        ([1, -1, 1, -1], 1),  # Mixed positive and negative numbers
        ([100, -100, 100, -100], 1),  # Large numbers
    ],
)
def test_array_sign_various_cases(nums, expected):
    solution = Solution()
    result = solution.arraySign(nums)
    assert result == expected
