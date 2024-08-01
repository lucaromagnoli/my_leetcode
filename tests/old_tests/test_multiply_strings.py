import pytest
from solutions.multiply_strings import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        ("2", "3", "6"),
        ("123", "456", "56088"),
        ("0", "12345", "0"),
        ("12345", "0", "0"),
        ("0", "0", "0"),
        ("0002", "003", "6"),
        ("000", "000", "0"),
    ],
)
def test_multiply(solution, num1, num2, expected):
    assert solution.multiply(num1, num2) == expected
