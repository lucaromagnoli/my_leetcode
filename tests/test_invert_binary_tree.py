import pytest
from solutions.invert_binary_tree import Solution, TreeNode

@pytest.fixture
def solution():
    return Solution()

def tree_to_list(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
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

def test_single_node_tree(solution):
    root = TreeNode(1)
    inverted = solution.invertTree(root)
    assert tree_to_list(inverted) == [1]

def test_complete_binary_tree(solution):
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inverted = solution.invertTree(root)
    assert tree_to_list(inverted) == [4, 7, 2, 9, 6, 3, 1]

def test_left_skewed_tree(solution):
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    inverted = solution.invertTree(root)
    assert tree_to_list(inverted) == [1, None, 2, None, 3, None, 4]

def test_right_skewed_tree(solution):
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    inverted = solution.invertTree(root)
    assert tree_to_list(inverted) == [1, 2, None, 3, None, 4]

def test_empty_tree(solution):
    root = None
    inverted = solution.invertTree(root)
    assert tree_to_list(inverted) == []

def test_mixed_tree(solution):
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    inverted = solution.invertTree(root)
    assert tree_to_list(inverted) == [2, 3, 1]