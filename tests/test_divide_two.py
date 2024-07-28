import pytest
from solutions.divide_two_int import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize(
    "dividend, divisor, expected",
    [
        pytest.param(10, 3, 3, id="Example 1"),
        pytest.param(7, -3, -2, id="Example 2"),
        pytest.param(0, 1, 0, id="Zero dividend"),
        pytest.param(1, 1, 1, id="Dividend equals divisor"),
        pytest.param(-10, -3, 3, id="Both negative"),
        pytest.param(2**31 - 1, 1, 2**31 - 1, id="Maximum positive dividend"),
        pytest.param(-2**31, 1, -2**31, id="Minimum negative dividend"),
        pytest.param(2**31 - 1, -1, -(2**31 - 1), id="Maximum positive dividend with negative divisor"),
        pytest.param(-2**31, -1, 2**31, id="Minimum negative dividend with negative divisor"),
    ],
)
def test_divides_correctly(solution, dividend, divisor, expected):
    result = solution.divide(dividend, divisor)
    assert result == expected