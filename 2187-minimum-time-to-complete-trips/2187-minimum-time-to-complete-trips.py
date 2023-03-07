class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        ans = 0
        L = 1
        R = int(10e17)
        while L <= R:
            mid = (L + R) // 2
            val = 0
            for i in range (len(time)):
                val += (mid // time[i])
            if val >= totalTrips: 
                ans = mid
                R = mid - 1
            else :
                L = mid + 1
        ###
        return ans