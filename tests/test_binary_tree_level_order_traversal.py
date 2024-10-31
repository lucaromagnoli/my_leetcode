import pytest
from solutions.binary_tree_level_order_traversal import Solution, TreeNode

@pytest.mark.parametrize(
    "root, expected_output",
    [
        (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), [[3], [9, 20], [15, 7]]),  # Example 1
        (TreeNode(1), [[1]]),  # Example 2
        (None, []),  # Example 3
        (TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5))), [[1], [2, 3], [4, 5]]),  # Unbalanced tree
        (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), [[1], [2, 3], [4]]),  # Left-heavy tree
        (TreeNode(1, None, TreeNode(2, None, TreeNode(3))), [[1], [2], [3]]),  # Right-heavy tree
        (TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))), [[1], [2, 3], [4, 5, 6, 7]]),  # Full binary tree
    ],
)
def test_level_order_traversal(root, expected_output):
    solution = Solution()
    assert solution.levelOrder(root) == expected_output