import pytest
from solutions.linked_list import iterable_to_list_node
from solutions.merge_two_sorted_lists import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], [""]),
        ([], [0], [0]),
        ([5], [1, 2, 4], [1, 2, 4, 5]),
    ],
)
def test_merge_two_lists(solution, list1, list2, expected):
    assert solution.mergeTwoLists(
        iterable_to_list_node(list1), iterable_to_list_node(list2)
    ) == iterable_to_list_node(expected)
