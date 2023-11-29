# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r_list = list()
        if root and root.val:
            r_list.extend(self.inorderTraversal(root.left))
            r_list.append(root.val)
            r_list.extend(self.inorderTraversal(root.right))
        return r_list

