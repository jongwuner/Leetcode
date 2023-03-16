# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def divideLR(inorder, postorder):
            # postorder의 마지막 값이 항상 루트다. answer에 삽입하고,
            # inorder에서 인덱스를 찾고, Lsubtree(5), Rsubtree(4) 개수를 파악해서, 
            # inorder에서는 [0:rootIdx], [rootIdx+1:]
            # postorder에서 [0:Lsubtree개수]를 postorder [5:-1]를 postorder. 항상 2개씩
            # 그 후, 재귀탐색한다.
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