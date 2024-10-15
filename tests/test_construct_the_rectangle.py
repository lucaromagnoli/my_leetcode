import pytest
from solutions.construct_the_rectangle import Solution


@pytest.mark.parametrize(
    "area, expected",
    [
        (4, [2, 2]),
        (37, [37, 1]),
        (122122, [427, 286]),
        (1, [1, 1]),  # Minimum area
        (2, [2, 1]),  # Prime number area
        (100, [10, 10]),  # Perfect square
        (9999991, [9999991, 1]),  # Large prime number
        (16, [4, 4]),  # Another perfect square
        (18, [6, 3]),  # Non-square even number
        (45, [9, 5]),  # Non-square odd number
    ],
)
def test_construct_rectangle_various_cases(area, expected):
    solution = Solution()
    result = solution.constructRectangle(area)
    assert result == expected
