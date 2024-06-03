# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = dict()
        self.bfs(root, parent)
        common_set = set()
        i = p
        while i:
            common_set.add(i)
            i = parent.get(i.val)
        i = q
        while i:
            if i in common_set:
                return i
            else:
                i = parent.get(i.val)

    def bfs(self, node: 'TreeNode', parent: 'dict'):
        if node.left:
            parent[node.left.val] = node
            self.bfs(node.left, parent)
        if node.right:
            parent[node.right.val] = node
            self.bfs(node.right, parent)
