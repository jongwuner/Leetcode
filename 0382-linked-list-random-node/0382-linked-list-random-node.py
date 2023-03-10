# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        
        now = head
        nodeNum = []
        
        while now != None:
            nodeNum.append(now.val)
            now = now.next
        
        self.size = len(nodeNum)
        self.nodes = nodeNum

    def getRandom(self) -> int:
        idx = random.randrange(0,self.size)
        return self.nodes[idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()