"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Title: Convert Sorted Array to Binary Search Tree
No: 108
Difficulty: Easy
Category: Algorithms
Problem:
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:


Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.


"""

from typing import Optional, List

from utils.data_structures import TreeNode


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 0:
            return None

        def inner(l, r) -> TreeNode:
            if l > r:
                return

            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            node.left = inner(l, mid - 1)
            node.right = inner(mid + 1, r)
            return node

        return inner(0, n - 1)
