# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def treeOrder(self, root, l, r):
        if root is None:
            return
        self.ans = max(self.ans, l, r)
        self.treeOrder(root.left, r + 1, 0)
        self.treeOrder(root.right, 0, l + 1)

    def longestZigZag(self, root: TreeNode) -> int:
        self.treeOrder(root, 0, 0)
        return self.ans