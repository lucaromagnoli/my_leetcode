"""
Utility module for linked list problems.
"""

class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"

    def __eq__(self, other):
        this = self
        while this and other:
            if other.val == this.val:
                this = this.next
                other = other.next
            else:
                return False
        return True


def iterable_to_list_node(iterable: list | tuple | str) -> ListNode:
    """Convert an iterable to a linked list."""
    if iterable:
        root = ListNode(val=iterable[0])
        previous = root
        for i in range(1, len(iterable)):
            current = ListNode(val=iterable[i])
            previous.next = current
            previous = current
        return root


def linked_list_to_list(node: ListNode) -> list:
    """Convert a linked list to a list."""
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values
