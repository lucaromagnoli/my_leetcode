import pytest
from solutions.convert_sorted_array_to_binary_search_tree import Solution
from utils.data_structures import tree_to_list


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-10, -3, 0, 5, 9], [0, -10, 5, None, -3, None, 9]),
        ([1, 3], [1, None, 3]),
        ([1], [1]),
        ([], []),
    ],
)
def test_sorted_array_to_bst_correctness(nums, expected):
    solution = Solution()
    root = solution.sortedArrayToBST(nums)
    assert tree_to_list(root) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1, 2, 3, 4, 5, 6], [3, 1, 5, 0, 2, 4, 6]),
        ([-1, 0, 1, 2], [0, -1, 1, None, None, None, 2]),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [5, 2, 7, 1, 3, 6, 8, None, None, None, 4, None, None, None, 9],
        ),
    ],
)
def test_sorted_array_to_bst_edge_cases(nums, expected):
    solution = Solution()
    root = solution.sortedArrayToBST(nums)
    assert tree_to_list(root) == expected
