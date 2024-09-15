import pytest
from solutions.binary_tree_postorder_traversal import Solution
from utils.data_structures import TreeNode


@pytest.fixture
def create_binary_tree():
    def _create_binary_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kid = nodes[::-1]
        root = kid.pop()
        for node in nodes:
            if node:
                if kid:
                    node.left = kid.pop()
                if kid:
                    node.right = kid.pop()
        return root

    return _create_binary_tree


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, None, 2, 3], [3, 2, 1]),
        ([], []),
        ([1], [1]),
    ],
)
def test_postorder_traversal_correctness(create_binary_tree, values, expected):
    root = create_binary_tree(values)
    solution = Solution()
    assert solution.postorderTraversal(root) == expected


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], [4, 5, 2, 6, 7, 3, 1]),
        ([1, None, 2, None, 3, None, 4], [4, 3, 2, 1]),
        ([1, 2, None, 3, None, 4, None], [4, 3, 2, 1]),
    ],
)
def test_postorder_traversal_edge_cases(create_binary_tree, values, expected):
    root = create_binary_tree(values)
    solution = Solution()
    assert solution.postorderTraversal(root) == expected
