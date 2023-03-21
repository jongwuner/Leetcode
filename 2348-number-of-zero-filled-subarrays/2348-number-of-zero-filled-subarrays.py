class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = 0
        ans = 0
        for i, num in enumerate(nums):
            if num == 0:
                cnt += 1
            elif num != 0 and cnt != 0:
                ans += (cnt * (cnt + 1)) // 2 
                cnt = 0
        ans += (cnt * (cnt + 1)) // 2
        return ans