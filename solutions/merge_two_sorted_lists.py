"""
https://leetcode.com/problems/merge-two-sorted-lists/
Title: Merge Two Sorted Lists
No: 21
Difficulty: Easy
Category: Algorithms
Problem:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.



"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def drain_list(self, source: ListNode, destination: ListNode):
        while source:
            destination.val = source.val
            source = source.next
            if source:
                destination.next = ListNode("")
                destination = destination.next

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        merged = ListNode("")
        next_node = merged
        while list1 and list2:
            if list1.val < list2.val:
                next_node.val = list1.val
                list1 = list1.next
            elif list1.val == list2.val:
                next_node.val = list1.val
                list1 = list1.next

                next_node.next = ListNode(list2.val)
                next_node = next_node.next
                list2 = list2.next
            else:
                next_node.val = list2.val
                list2 = list2.next

            if list1 or list2:
                next_node.next = ListNode("")
                next_node = next_node.next
        if list1 and not list2:
            self.drain_list(list1, next_node)
        elif list2 and not list1:
            self.drain_list(list2, next_node)

        return merged
