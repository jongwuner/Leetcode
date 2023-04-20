# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        queue = []
        queue.append((0, root))
        while queue:
            ans = max(ans, queue[-1][0] - queue[0][0] + 1)
            nextQ = []
            while queue:
                index, node = queue.pop(0)
                if node.left:
                    nextQ.append((2*index, node.left))
                if node.right:
                    nextQ.append((2*index+1, node.right))
            queue = nextQ
        return ans
                