# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if hasattr(head, "is_visit"):
                return True
            else:
                head.is_visit = True
            head = head.next
        return False
    # 快慢指针方式
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        if not head and not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast and not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
