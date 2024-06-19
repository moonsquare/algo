from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def mybuildTree(pre_start: int, in_start: int, in_end: int) -> Optional[TreeNode]:
            if in_start > in_end:
                return
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            if in_start == in_end:
                return root
            # 记录逻辑，后面是优化后的代码，显的更短
            # left_num = index[root_val] - in_start
            # left_in_start = in_start
            # left_in_end = index[root_val] - 1
            # right_in_start = index[root_val] + 1
            # right_in_end = in_end
            # left_pre_start = pre_start + 1
            # right_pre_start = left_pre_start + left_num
            root_idx = index[root_val]
            root.left = mybuildTree(pre_start + 1, in_start, root_idx - 1)
            root.right = mybuildTree(pre_start + root_idx - in_start + 1, root_idx + 1, in_end)
            return root

        # 构建中序中的根节点位置
        index = {element: i for i, element in enumerate(inorder)}
        start, end = 0, len(preorder) - 1
        return mybuildTree(0, 0, len(preorder) - 1)
