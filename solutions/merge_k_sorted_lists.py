"""
https://leetcode.com/problems/merge-k-sorted-lists/
Title: Merge k Sorted Lists
No: 23
Difficulty: Hard
Category: Algorithms
Problem:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
 
Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

 
Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.


"""

from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list_to_list(node: ListNode) -> list:
    """Convert a linked list to a list."""
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


def list_to_list_node(iterable: list) -> ListNode:
    """Convert an iterable to a linked list."""
    if iterable:
        root = ListNode(val=iterable[0])
        previous = root
        for i in range(1, len(iterable)):
            current = ListNode(val=iterable[i])
            previous.next = current
            previous = current
        return root


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        lists = sorted(
            [
                l
                for iterable in [linked_list_to_list(l) for l in lists]
                for l in iterable
            ]
        )
        return list_to_list_node(lists)
