# Definition for singly-linked list.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        k_head = ListNode()
        k_head.next = head
        self.reverseKNodes(k_head, k)
        return k_head.next

    def reverseKNodes(self, k_head, k, back=False):
        first_node = k_head.next
        if first_node:
            reverse_node = first_node.next
            pre_node = first_node
            for i in range(k - 1):
                if reverse_node:
                    next_node = reverse_node.next
                    reverse_node.next = pre_node
                    pre_node = reverse_node
                    reverse_node = next_node
                # 如果不够k个元素，再反转回来
                elif not back:
                    k_head.next = pre_node
                    first_node.next = reverse_node
                    self.reverseKNodes(k_head, k, True)
                    # 已反转完毕退出
                    return
            first_node.next = reverse_node
            k_head.next = pre_node
            # 如果不够k个元素的反转，则退出递归
            if back:
                return
            self.reverseKNodes(first_node, k)


head = ListNode(0)
current = head
for i in range(1, 7):
    current.next = ListNode(i)
    current = current.next
solution = Solution()
# 调用反转函数
current = solution.reverseKGroup(head.next, 3)
while current:
    print(current.val, end=" ")
    current = current.next
