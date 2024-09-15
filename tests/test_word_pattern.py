import pytest
from solutions.word_pattern import Solution


@pytest.mark.parametrize(
    "pattern, s, expected",
    [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
        ("abba", "dog dog dog dog", False),
        ("abc", "dog cat fish", True),
    ],
)
def test_word_pattern_correctness(pattern, s, expected):
    solution = Solution()
    assert solution.wordPattern(pattern, s) == expected


@pytest.mark.parametrize(
    "pattern, s, expected",
    [
        ("", "", True),
        ("a", "dog", True),
        ("a", "", False),
        ("", "dog", False),
        ("ab", "dog", False),
    ],
)
def test_word_pattern_edge_cases(pattern, s, expected):
    solution = Solution()
    assert solution.wordPattern(pattern, s) == expected
