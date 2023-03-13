# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        global que1, que2
        que1 = []
        que2 = []
        
        def LDFS(root, visited):
            if root == None:
                que1.append('null')
                return
            
            visited.add(root)
            que1.append(root.val)
            
            if not root.left in visited:
                LDFS(root.left, visited)
            if not root.right in visited:
                LDFS(root.right, visited)
            
            
        def RDFS(root, visited):
            if root == None:
                que2.append('null')
                return
            
            visited.add(root)
            que2.append(root.val)
            if not root.right in visited:
                RDFS(root.right, visited)
            if not root.left in visited:
                RDFS(root.left, visited)
        
        visited = set()
        LDFS(root, visited)
        
        visited.clear()
        RDFS(root, visited)
        
        return que1 == que2
            