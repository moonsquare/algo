from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pre = dummy = ListNode()
        while True:
            if list1 and list2:
                if list1.val < list2.val:
                    pre.next = list1
                    pre = list1
                    list1 = list1.next
                else:
                    pre.next = list2
                    pre = list2
                    list2 = list2.next
            elif list1:
                pre.next = list1
                return dummy.next
            else:
                pre.next = list2
                return dummy.next
