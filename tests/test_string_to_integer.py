import pytest

from solutions.string_to_integer_8 import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "string, expected",
    [
        ("42", 42),
        ("-042", -42),
        ("1337c0d3", 1337),
        ("0-1", 0),
        ("words and 987", 0),
        ("-91283472332", -91283472332),
    ],
)
def test_solution(solution, string, expected):
    assert solution.myAtoi(string) == expected
