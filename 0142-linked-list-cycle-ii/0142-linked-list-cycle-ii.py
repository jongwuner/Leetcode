# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()        
        now = head;
        while now != None:
            if now in visited: 
                return now
            visited.add(now)
            now = now.next
        return None