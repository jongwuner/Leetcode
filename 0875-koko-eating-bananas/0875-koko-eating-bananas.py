class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = 0
        L = 1
        R = int(10e17)

        while L<=R :
            mid = (L + R) // 2

            val = 0
            for i in range(len(piles)):
               val += piles[i] // mid
               if piles[i] % mid > 0:
                    val += 1 
            if val <= h : 
                ans = mid
                R = mid - 1
            else :
                L = mid + 1
        return ans
