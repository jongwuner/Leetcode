class Solution:
    def arraySign(self, nums: List[int]) -> int:
        mul = 1
        for num in nums:
            mul *= num
        
        if mul > 0: return 1
        elif mul == 0: return 0
        elif mul < 0 : return -1