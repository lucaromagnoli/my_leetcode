"""
https://leetcode.com/problems/binary-tree-postorder-traversal/
Title: Binary Tree Postorder Traversal
No: 145
Difficulty: Easy
Category: Algorithms
Problem:
Given the root of a binary tree, return the postorder traversal of its nodes' values.
 
Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

 
Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

 
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import Optional, List

from utils.data_structures import TreeNode


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree = root
        solutions = []
        def inner(node):
            if node is None:
                return
            inner(node.left)
            inner(node.right)
            solutions.append(node.val)
        inner(tree)
        return solutions

        