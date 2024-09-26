import pytest
from solutions.substrings_of_size_three_with_distinct_characters import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("xyzzaz", 1),
        ("aababcabc", 4),
        ("abcabcabc", 7),
    ],
)
def test_count_good_substrings_correctness(s, expected):
    solution = Solution()
    result = solution.countGoodSubstrings(s)
    assert result == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("", 0),
        ("a", 0),
        ("ab", 0),
        ("aaa", 0),
        ("abc", 1),
    ],
)
def test_count_good_substrings_edge_cases(s, expected):
    solution = Solution()
    result = solution.countGoodSubstrings(s)
    assert result == expected
