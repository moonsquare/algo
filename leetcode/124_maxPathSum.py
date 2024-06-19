# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.maxSum = -sys.maxsize

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def curGain(node):
            if not node:
                return 0
            leftGain = curGain(node.left)
            rightGain = curGain(node.right)
            cur_Gain = max(max(leftGain, rightGain) + node.val, 0)
            self.maxSum = max(self.maxSum, node.val + leftGain + rightGain)
            return cur_Gain

        curGain(root)
        return self.maxSum
