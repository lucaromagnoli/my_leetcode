import pytest
from solutions.generate_parentheses import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("n, expected", [
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),  # Example 1
    (1, ["()"]),  # Example 2
    (2, ["(())", "()()"]),  # Two pairs
    (4, ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]),  # Four pairs
    (0, [""]),  # Zero pairs
])
def test_generates_correct_parentheses(solution, n, expected):
    assert sorted(solution.generateParenthesis(n)) == sorted(expected)
