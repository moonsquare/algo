from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = None

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.dfs(root, 0)
        return self.ans

    def dfs(self, node: Optional[TreeNode], depth):
        if not node:
            return
        if len(self.ans) == depth:
            self.ans.append(node.val)
        self.dfs(node.right, depth + 1)
        self.dfs(node.left, depth + 1)
        pass
