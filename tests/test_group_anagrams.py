import pytest
from solutions.group_anagrams import Solution


@pytest.mark.parametrize(
    "strs, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_group_anagrams_correctness(strs, expected):
    solution = Solution()
    result = solution.groupAnagrams(strs)
    assert sorted([sorted(group) for group in result]) == sorted(
        [sorted(group) for group in expected]
    )


@pytest.mark.parametrize(
    "strs, expected",
    [
        ([], []),
        (["a", "b", "c"], [["a"], ["b"], ["c"]]),
        (
            ["abc", "bca", "cab", "bac", "acb", "cba"],
            [["abc", "bca", "cab", "bac", "acb", "cba"]],
        ),
        (["", ""], [["", ""]]),
        (["ddddddddddg","dgggggggggg"], [["ddddddddddg"],["dgggggggggg"]])
    ],
)
def test_group_anagrams_edge_cases(strs, expected):
    solution = Solution()
    result = solution.groupAnagrams(strs)
    assert sorted([sorted(group) for group in result]) == sorted(
        [sorted(group) for group in expected]
    )
