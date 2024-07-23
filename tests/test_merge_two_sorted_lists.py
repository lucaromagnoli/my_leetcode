import pytest
from solutions.linked_list import iterable_to_list_node
from solutions.merge_two_sorted_lists import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),  # Both lists with same length
    ([], [], []),  # Both lists empty
    ([], [0], [0]),  # Second list with one element
    ([5], [1, 2, 4], [1, 2, 4, 5]),  # First list with one element
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),  # No matching elements
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),  # All elements of list1 come before list2
    ([4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5, 6]),  # All elements of list2 come before list1
    ([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]),  # All elements in both lists are the same
])
def test_merge_two_lists(solution, list1, list2, expected):
    assert solution.mergeTwoLists(
        iterable_to_list_node(list1), iterable_to_list_node(list2)
    ) == iterable_to_list_node(expected)
