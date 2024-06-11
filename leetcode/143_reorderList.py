# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        temp = []
        node = head
        while node:
            temp.append(node)
            node = node.next
        i, j = 0, len(temp) - 1
        while i < j:
            temp[i].next = temp[j]
            i += 1
            if i < j:
                temp[j].next = temp[i]
            elif i == j:
                temp[j].next = None
            j -= 1
        if i == j:
            temp[i].next = None
