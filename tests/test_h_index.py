import pytest
from solutions.h_index import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("citations, expected", [
    ([3, 0, 6, 1, 5], 3),
    ([1, 3, 1], 1),
    ([0, 0, 0, 0], 0),
    ([10, 8, 5, 4, 3], 4),
    ([25, 8, 5, 3, 3], 3),
    ([100], 1),
    ([0], 0),
    [[1, 2], 1]


])
def test_returns_correct_h_index(solution, citations, expected):
    assert solution.hIndex(citations) == expected
