import pytest
from solutions.combination_sum import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize(
    "candidates, target, expected",
    [
        pytest.param([2, 3, 6, 7], 7, [[2, 2, 3], [7]], id="Example 1"),
        pytest.param([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]], id="Example 2"),
        pytest.param([2], 1, [], id="Example 3"),
        pytest.param([1], 1, [[1]], id="Single element equals target"),
        pytest.param([1, 2], 4, [[1, 1, 1, 1], [1, 1, 2], [2, 2]], id="Multiple combinations"),
        pytest.param([2, 3, 5], 0, [[]], id="Target zero"),
        pytest.param([2, 3, 5], 1, [], id="Target less than smallest candidate"),
        pytest.param([2, 3, 5], 10, [[2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 3, 5], [5, 5]], id="Larger target"),
    ],
)
def test_combination_sum_scenarios(solution, candidates, target, expected):
    result = solution.combinationSum(candidates, target)
    assert sorted(result) == sorted(expected)
