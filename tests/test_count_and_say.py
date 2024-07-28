import pytest
from solutions.count_and_say import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(1, "1", id="Base case"),
        pytest.param(2, "11", id="Second element"),
        pytest.param(3, "21", id="Third element"),
        pytest.param(4, "1211", id="Fourth element"),
        pytest.param(5, "111221", id="Fifth element"),
        pytest.param(6, "312211", id="Sixth element"),
        pytest.param(7, "13112221", id="Seventh element"),
        pytest.param(8, "1113213211", id="Eighth element"),
        pytest.param(9, "31131211131221", id="Ninth element"),
        pytest.param(10, "13211311123113112211", id="Tenth element"),
    ],
)
def test_count_and_say_sequence(solution, n, expected):
    result = solution.countAndSay(n)
    assert result == expected
