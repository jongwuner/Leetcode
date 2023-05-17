# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Initialize a pointer and an array
        p = head
        values = []

        # Traverse the linked list, populate the array with the values
        while p:
            values.append(p.val)
            p = p.next

        # Initialize two pointers and max_twin_sum
        i, j = 0, len(values) - 1
        max_twin_sum = 0

        # Move the pointers toward each other and find the maximum twin sum
        while i < j:
            max_twin_sum = max(max_twin_sum, values[i] + values[j])
            i += 1
            j -= 1

        return max_twin_sum
