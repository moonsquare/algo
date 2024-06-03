from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa, pb = headA, headB
        # pa, pb = headA, headB
        # if pa == pb :
        #     print(2)
        while pa != pb:
            if pa:
                pa = pa.next
            else:
                pa = headB
            if pb:
                pb = pb.next
            else:
                pb = headA
        return pa
headA = ListNode(1)
headB = ListNode(2)
sl = Solution()
sl.getIntersectionNode(headA,headB)
