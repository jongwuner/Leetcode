# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        count = collections.Counter()

        def search(root):

            if not root: 
                return 'NULL'

            chk_str = str(root.val) +','+search(root.left) +','+ search(root.right)
            count[chk_str] += 1
            if count[chk_str] == 2:
                res.append(root)
            return chk_str

        search(root)
        return res