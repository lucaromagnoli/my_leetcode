"""
https://leetcode.com/problems/invert-binary-tree/
Title: Invert Binary Tree
No: 226
Difficulty: Easy
Category: Algorithms
Problem:
Given the root of a binary tree, invert the tree, and return its root.
 
Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:


Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root

        def invert(tree_node):
            if tree_node is None:
                return
            tree_node.left, tree_node.right = tree_node.right, tree_node.left

            invert(tree_node.left)
            invert(tree_node.right)

        invert(node)
        return node