# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def getAnswer(nums):
            if len(nums) == 1:
                return TreeNode(nums[0].val, None, None)
            if len(nums) < 1:
                return None
            
            root_idx = len(nums) // 2
        
            left_child = getAnswer(nums[0:root_idx])
            right_child = getAnswer(nums[root_idx+1:])
        
            return TreeNode(nums[root_idx].val, left_child, right_child)
        
        now = head
        nums = []
        
        while now != None: # 길이재기
            nums.append(now)
            now = now.next
        
        return getAnswer(nums)