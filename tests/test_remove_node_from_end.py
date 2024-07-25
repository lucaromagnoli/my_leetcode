import pytest
from solutions.remove_node_from_end import Solution
from solutions.linked_list import iterable_to_list_node, linked_list_to_list

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("input_list, n, expected", [
    ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),  # Remove from middle
    ([1], 1, []),  # Single element
    ([1, 2], 1, [1]),  # Remove last element
    ([1, 2], 2, [2]),  # Remove first element
    ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),  # Remove very first element
    ([1, 2, 3, 4, 5, 6], 3, [1, 2, 3, 5, 6]),  # Remove exact middle element in even list
][5:6])
def test_remove_nth_from_end(solution, input_list, n, expected):
    head = iterable_to_list_node(input_list)
    result_head = solution.removeNthFromEnd(head, n)
    assert linked_list_to_list(result_head) == expected