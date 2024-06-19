from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween_1(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        pre = dummy = ListNode()
        dummy.next = head
        for _ in range(left - 1):
            pre = pre.next
        first = pre.next
        for _ in range(right - left):
            cur = first.next
            first.next = cur.next
            cur.next = pre.next
            pre.next = cur
        return dummy.next


    def reverseBetween_2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        pre = dummy = ListNode()
        dummy.next = first = it_node = head
        i = 1
        while i < right:
            if i < left:
                dummy = it_node
                first = dummy.next
            else:
                dummy.next = it_node.next
                it_node.next = pre
            pre = it_node
            it_node = dummy.next
            i += 1
        first.next = it_node.next
        it_node.next = pre
        if left == 1:
            return dummy.next
        else:
            return head

so = Solution()
head = node = ListNode(1)
i = 2
while i < 6:
    node.next = ListNode(i)
    node = node.next
    i += 1
so.reverseBetween(head, 2, 4)
