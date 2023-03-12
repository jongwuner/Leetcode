# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newList = []
        for tlist in lists:
            now = tlist
            while now != None:
                newList.append(now)
                now = now.next
        if len(newList) < 1:
            return None  
        
        newList = sorted(newList, key=lambda x: x.val)

        for i in range(1, len(newList)):
            newList[i-1].next = newList[i]
        
        return newList[0]