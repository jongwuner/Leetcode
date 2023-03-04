class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        outIdx = -1
        minKIdx = -1
        maxKIdx = -1
        length = nums.__len__()

        for i in range (length):
            if nums[i] == minK:
                minKIdx = i
            if nums[i] == maxK:
                maxKIdx = i
            if nums[i] < minK or nums[i] > maxK:
                outIdx = i

            added = min(minKIdx, maxKIdx) - outIdx
            ans += added if added > 0 else 0
        return ans