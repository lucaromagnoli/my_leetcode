"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
Title: Binary Tree Level Order Traversal
No: 102
Difficulty: Medium
Category: Algorithms
Problem:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
 
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

 
Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000


"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        stack = [[root]]
        values = []

        while stack:
            level_values = []
            level_nodes = []
            nodes = stack.pop()
            for node in nodes:
                if node:
                    level_values.append(node.val)
                    if node.left:
                        level_nodes.append(node.left)
                    if node.right:
                        level_nodes.append(node.right)
            if level_values:
                values.append(level_values)
            if level_nodes:
                stack.append(level_nodes)

        return values
