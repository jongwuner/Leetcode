class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = 0
        for i, num in enumerate(nums):
            if num * 2 > target: continue
            val = target - num
            L = i
            R = len(nums) - 1
            ansIdx = i
            while L <= R:
                mid = (L + R) // 2
                if nums[mid] <= val:
                    ansIdx = mid
                    L = mid + 1
                else:
                    R = mid - 1
            ans = (ans + 2 ** (ansIdx - i)) % (int(1e9 + 7))
        return int(ans)