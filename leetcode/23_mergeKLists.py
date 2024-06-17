import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode(0)
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i]))
        while h:
            val, curNode = heapq.heappop(h)
            ans.next = curNode
            ans = curNode
            if curNode.next:
                heapq.heappush(h, (curNode.next.val, curNode))


so = Solution()
l = ListNode()
l.val = 1
t = ListNode()
t.val = 0
lists = [l, t]
so.mergeKLists(lists)
