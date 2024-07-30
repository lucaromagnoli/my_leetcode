"""
"https://leetcode.com/problems/add-two-numbers"
Title: Add Two Numbers
No: 2
Difficulty: Medium
Category: Algorithms
Problem:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 
Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

 
Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.


"""
from typing import Optional

from utils.linked_list import ListNode


class Solution:

    def get_values(self, list_node: ListNode):

        def inner(node):
            while node:
                yield node.val
                node = node.next

        return list(inner(list_node))

    def get_number(self, digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i] * 10**i
        return num

    def number_to_linked_list(self, num: int):
        rev_digits = [int(i) for i in reversed(str(num))]
        val = rev_digits.pop(0)
        root = ListNode(val)
        previous = root
        for d in rev_digits:
            node = ListNode(d)
            previous.next = node
            previous = node
        return root
