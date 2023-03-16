# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def divideLR(inorder, postorder):
            if len(postorder) == 0:
                return None
            if len(postorder) == 1:
                return TreeNode(postorder[0])
            
            root = TreeNode(postorder[-1])
            rootIdx = inorder.index(postorder[-1])
            
            leftInorder = inorder[0:rootIdx]
            rightInorder = inorder[rootIdx+1:]
            leftPostorder = postorder[0:rootIdx]
            rightPostorder = postorder[rootIdx:-1]

            root.left = divideLR(leftInorder, leftPostorder)
            root.right = divideLR(rightInorder, rightPostorder)
            return root

        return divideLR(inorder, postorder)
