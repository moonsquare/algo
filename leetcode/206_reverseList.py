# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            next = head.next
            head.next = None
            return self.reversedListNode(next, head)
        else:
            return head

    def reversedListNode(self, reverse_node: Optional[ListNode], pre_node: Optional[ListNode]) -> Optional[ListNode]:
        if reverse_node:
            next_node = reverse_node.next
            reverse_node.next = pre_node
            return self.reversedListNode(next_node, reverse_node)
        else:
            return pre_node


head = [1, 2, 3, 4, 5]
n = ListNode(head[0])
head_n = n
for i in range(1, len(head)):
    next = ListNode(head[i])
    n.next = next
    n = next
s = Solution()
n = s.reverseList(head_n)

while n:
    print(n.val, " ")
    n = n.next
