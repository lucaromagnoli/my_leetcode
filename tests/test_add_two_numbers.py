import pytest
from solutions.add_two_numbers import Solution
from solutions.linked_list import iterable_to_list_node, linked_list_to_list


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "input1, input2, expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),  # Example 1
        ([0], [0], [0]),  # Example 2
        (
            [9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9],
            [8, 9, 9, 9, 0, 0, 0, 1],
        ),  # Example 3
        ([], [0], [0]),  # One empty list
        ([1], [], [1]),  # Other empty list
        ([9, 9], [1], [0, 0, 1]),  # Carry over beyond the length of one list
    ],
)
def test_add_two_numbers(solution, input1, input2, expected):
    l1 = iterable_to_list_node(input1)
    l2 = iterable_to_list_node(input2)
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == expected
