import pytest
from solutions.generate_parenthesis import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "n, expected",
    [
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),  # Example 1
        (1, ["()"]),  # Example 2
        (0, []),  # Edge case: n = 0
        (2, ["(())", "()()"]),  # Small n
        (
            4,
            [
                "(((())))",
                "((()()))",
                "((())())",
                "((()))()",
                "(()(()))",
                "(()()())",
                "(()())()",
                "(())(())",
                "(())()()",
                "()((()))",
                "()(()())",
                "()(())()",
                "()()(())",
                "()()()()",
            ],
        ),  # Larger n
    ],
)
def test_generate_parenthesis(solution, n, expected):
    result = solution.generateParenthesis(n)
    assert sorted(result) == sorted(expected)
