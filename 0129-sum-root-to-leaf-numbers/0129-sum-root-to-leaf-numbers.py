# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def postOrder(root) -> list:
            if root.left == None and root.right == None:
                return [str(root.val)]
            numList = []
            if root.left: #left 존재할 경우
                numList.extend(postOrder(root.left))
            if root.right: #right 존재할 경우
                numList.extend(postOrder(root.right))
            for i, num in enumerate(numList):
                numList[i] = str(root.val) + numList[i]
            return numList
        
        numList = postOrder(root)
        for i, num in enumerate(numList):
            numList[i] = int(num)
        return sum(numList)