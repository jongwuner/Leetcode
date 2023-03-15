# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        global visited, que, answer
        answer = [root.val]
        que = deque()
        que.append(root)
        
        def bfs(root):
            while len(que) > 0:
                now = que.popleft()

                if now.left:
                    que.append(now.left)
                    answer.append(now.left.val)
                else:
                    answer.append(None)
                    
                if now.right:
                    que.append(now.right)
                    answer.append(now.right.val)
                else:
                    answer.append(None)
        
        bfs(root)
        flag = True
        for i, node in enumerate(answer):
            if node == None:
                flag = False
            elif flag == False and node != None:
                return False
        return True
        
