import pytest
from solutions.pascals_triangle_ii import Solution


@pytest.mark.parametrize(
    "rowIndex, expected",
    [
        (3, [1, 3, 3, 1]),
        (0, [1]),
        (1, [1, 1]),
    ],
)
def test_get_row_correctness(rowIndex, expected):
    solution = Solution()
    assert solution.getRow(rowIndex) == expected


@pytest.mark.parametrize(
    "rowIndex, expected",
    [
        (4, [1, 4, 6, 4, 1]),
        (5, [1, 5, 10, 10, 5, 1]),
        (6, [1, 6, 15, 20, 15, 6, 1]),
    ],
)
def test_get_row_edge_cases(rowIndex, expected):
    solution = Solution()
    assert solution.getRow(rowIndex) == expected
