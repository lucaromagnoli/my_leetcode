"""
Utility module for linked list problems.
"""

from lib2to3.pytree import Node


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self._node = None

    def traverse_binary_tree(self):
        if not self:
            return []
        result, queue = [], [self]
        while any(queue):
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result

    def __repr__(self):
        return f"          {self.val}\n" f"{self.left}         {self.right}\n"


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


def iterable_to_treenode(items: list[int]) -> TreeNode:
    """Create binary tree from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


def tree_to_list(root):
    """Convert binary tree to list."""
    if not root:
        return []
    result, queue = [], [root]
    while any(queue):
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result
