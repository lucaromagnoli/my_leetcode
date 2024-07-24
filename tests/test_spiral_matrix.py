import pytest
from solutions.spiral_matrix import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("n, expected_output", [
    (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),  # Standard 3x3 matrix
    (1, [[1]]),  # Single element matrix
    (4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]),  # 4x4 matrix
    (2, [[1, 2], [4, 3]]),  # 2x2 matrix
    (5, [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]),  # 5x5 matrix
])
def test_generate_matrix(solution, n, expected_output):
    assert solution.generateMatrix(n) == expected_output