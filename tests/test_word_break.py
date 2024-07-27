import pytest
from solutions.word_break import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "s, wordDict, expected",
    [
        ("leetcode", ["leet", "code"], True),  # Example 1
        ("applepenapple", ["apple", "pen"], True),  # Example 2
        (
            "catsandog",
            ["cats", "dog", "sand", "and", "cat"],
            False,
        ),  # Example 3
        ("", ["a", "b"], False),  # Edge case: empty string
        ("a", [], False),  # Edge case: empty dictionary
        ("a", ["a"], True),  # Single character match
        ("aaaaaaa", ["aaaa", "aaa"], True),  # Reuse dictionary words
        ("aaaaaaa", ["aaaa", "aa"], False),  # No valid segmentation,
        ("bb", ["a", "b", "bbb", "bbbb"], True),
        (
            "pineapplepenapple",
            ["apple", "pen", "applepen", "pine", "pineapple"],
            True,
        ),  # Complex case
        ("cars", ["car", "ca", "rs"], True),
        ("dogs", ["dog", "s", "gs"], True),
        (
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            [
                "a",
                "aa",
                "aaa",
                "aaaa",
                "aaaaa",
                "aaaaaa",
                "aaaaaaa",
                "aaaaaaaa",
                "aaaaaaaaa",
                "aaaaaaaaaa",
            ],
            False,
        ),
        (
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            [
                "aa",
                "aaa",
                "aaaa",
                "aaaaa",
                "aaaaaa",
                "aaaaaaa",
                "aaaaaaaa",
                "aaaaaaaaa",
                "aaaaaaaaaa",
                "ba",
            ],
            False,
        ),
        ("a", ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa"], False),
    ][:],
)
def test_word_break(solution, s, wordDict, expected):
    result = solution.wordBreak(s, wordDict)
    assert result == expected
