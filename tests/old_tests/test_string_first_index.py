import pytest
from solutions.string_first_index import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "haystack, needle, expected",
    [
        ("sadbutsad", "sad", 0),  # Needle at the beginning
        ("leetcode", "leeto", -1),  # Needle not in haystack
        ("hello", "ll", 2),  # Needle in the middle
        ("aaaaa", "bba", -1),  # Needle completely absent
        ("a", "a", 0),  # Single character needle found at the beginning
        ("mississippi", "issip", 4),  # Needle occurs after initial characters
        ("mississippi", "issippi", 4),  # Needle is the latter part of haystack
        (
            "mississippi",
            "sippia",
            -1,
        ),  # Almost entire needle present but one character mismatch
    ],
)
def test_strStr(solution, haystack, needle, expected):
    r = solution.strStr(haystack, needle)
    assert r == expected, f"Expected {expected}. Got {r}"
