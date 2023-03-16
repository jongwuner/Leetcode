# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            def divideLR(preorder, inorder):
                if len(preorder) == 0:
                    return None
                if len(preorder) == 1:
                    return TreeNode(preorder[0])

                root = TreeNode(preorder[0])
                rootIdx = inorder.index(preorder[0])

                Lpreorder = preorder[1:1+rootIdx]
                Linorder = inorder[0:rootIdx]

                Rpreorder = preorder[1+rootIdx:]
                Rinorder = inorder[rootIdx+1:]

                root.left = divideLR(Lpreorder, Linorder)
                root.right = divideLR(Rpreorder, Rinorder)
                return root
            return divideLR(preorder, inorder)