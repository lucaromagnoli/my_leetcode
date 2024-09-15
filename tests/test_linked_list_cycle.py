import pytest
from solutions.linked_list_cycle import Solution
from utils.data_structures import ListNode


@pytest.fixture
def create_linked_list():
    def _create_linked_list(values, pos):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        cycle_node = None
        for i in range(1, len(values)):
            current.next = ListNode(values[i])
            current = current.next
            if i == pos:
                cycle_node = current
        if pos != -1:
            current.next = cycle_node
        return head

    return _create_linked_list


@pytest.mark.parametrize(
    "values, pos, expected",
    [
        ([3, 2, 0, -4], 1, True),
        ([1], -1, False),
    ],
)
def test_has_cycle_correctness(create_linked_list, values, pos, expected):
    head = create_linked_list(values, pos)
    solution = Solution()
    assert solution.hasCycle(head) == expected


@pytest.mark.parametrize(
    "values, pos, expected",
    [
        ([], -1, False),
        ([1, 2, 3, 4, 5], -1, False),
        ([1, 2, 3, 4, 5], 4, True),
    ],
)
def test_has_cycle_edge_cases(create_linked_list, values, pos, expected):
    head = create_linked_list(values, pos)
    solution = Solution()
    assert solution.hasCycle(head) == expected
