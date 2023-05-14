from typing import List
from math import gcd
from functools import lru_cache

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums) // 2
        @lru_cache(None)
        def dp(mask):
            if mask == 0:
                return 0
            ans = 0
            for i in range(2 * n):
                if mask & (1 << i):
                    for j in range(i + 1, 2 * n):
                        if mask & (1 << j):
                            ans = max(ans, dp(mask ^ (1 << i) ^ (1 << j)) + (bin(mask).count('1') // 2) * gcd(nums[i], nums[j]))
            return ans
        return dp((1 << (2 * n)) - 1)
