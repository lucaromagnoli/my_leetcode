import pytest
from solutions.check_if_every_row_and_column_contains_all_numbers import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2, 3], [3, 1, 2], [2, 3, 1]], True),  # Example 1
        ([[1, 1, 1], [1, 2, 3], [1, 2, 3]], False),  # Example 2
        ([[1]], True),  # Single element matrix
        ([[1, 2], [2, 1]], True),  # 2x2 valid matrix
        ([[1, 2], [1, 2]], False),  # 2x2 invalid matrix
        (
            [[1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 4, 3], [3, 4, 1, 2]],
            True,
        ),  # 4x4 valid matrix
        (
            [[1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 4, 3], [3, 4, 1, 1]],
            False,
        ),  # 4x4 invalid matrix with duplicate
        (
            [[1, 2, 3], [3, 1, 2], [2, 3, 4]],
            False,
        ),  # 3x3 invalid matrix with out of range number
        ([[1, 2, 3], [3, 1, 2], [2, 3, 0]], False),  # 3x3 invalid matrix with zero
        ([[1, 2, 3], [3, 1, 2], [2, 3, 1], [4, 4, 4]], False),  # 4x3 invalid matrix
    ],
)
def test_returns_if_matrix_is_valid(solution, matrix, expected):
    assert solution.checkValid(matrix) == expected
