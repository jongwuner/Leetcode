class Solution(object):
    def minimumDeviation(self, nums):
        ans = int(10e9 + 9)
        N = nums.__len__()

        minHeap = []
        maxHeap = []

        for i in range(N):
            if nums[i] % 2 == 1:
                nums[i] *= 2
            heappush(minHeap, nums[i])        
            heappush(maxHeap, -nums[i])


        tmax = -maxHeap[0]
        tmin = minHeap[0]

        while tmin <= tmax :
            ans = min(ans, tmax - tmin)
            if tmax % 2 == 0:
                heappop(maxHeap)
                heappush(minHeap, int(tmax/2))
                heappush(maxHeap, int(-tmax/2))
            else:
                break

            tmax = -maxHeap[0]
            tmin = minHeap[0]
        
        return ans
