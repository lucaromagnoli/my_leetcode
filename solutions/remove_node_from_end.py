"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
"""
from typing import Optional

from solutions.linked_list import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lnk_list = list(self.iter_linked_list(head))
        lnk_list.pop(len(lnk_list) - n)
        if not lnk_list:
            return None
        head = ListNode(val=lnk_list[0])
        node = head
        for i in lnk_list[1:]:
            node.next = ListNode(val=i)
            node = node.next
        return head
    def iter_linked_list(self, node):
        while node:
            yield node.val
            node = node.next

