from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 一共有3种思路
# 1、遍历连链表，放入数组，通过同时遍历前指针和后指针进行比对开是否回文。（空间O（n）
# 2、递归方式的双指针，通过递归调用，比对首尾的值。（归根结底还是栈）（空间O（n））
# 3、快慢指针，找到链表的中间节点，然后反转后半部分，然后对比判断是否回文【空间O（1）】
# 下面使用递归方式实现
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.pointer = head

        def check_palindrome(current_node=head) -> bool:
            if not current_node:
                return True
            if check_palindrome(current_node.next) and current_node.val == self.pointer.val:
                self.pointer = self.pointer.next
                return True
            return False

        return check_palindrome()
