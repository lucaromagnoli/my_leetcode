from typing import Optional

from linked_list import iterable_to_list_node, ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        root = head
        while root:
            previous_node, next_node = root, root.next
            previous_node.val, next_node.val = next_node.val, previous_node.val
            root = next_node.next
        return head


if __name__ == "__main__":
    s = Solution()
    head = iterable_to_list_node([])
    r = s.swapPairs(head)
    print(r)
