# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Initialize pointers
        forward = head
        backward = head
        length = 0

        # Compute the length of the linked list
        temp = head
        while temp:
            length += 1
            temp = temp.next

        # Get the kth node from the beginning
        for _ in range(k - 1):
            forward = forward.next

        # Get the kth node from the end
        for _ in range(length - k):
            backward = backward.next

        # Swap the values at the forward and backward pointers
        forward.val, backward.val = backward.val, forward.val

        return head