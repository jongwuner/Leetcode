class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        sum = 0
        max = 0
        for i, num in enumerate(nums): 
            sum += num
            if max < num:
                if (sum // (i + 1)) >= max:
                    max = sum // (i + 1) + 1 if sum % (i + 1) > 0 else sum // (i + 1) 
        return max
