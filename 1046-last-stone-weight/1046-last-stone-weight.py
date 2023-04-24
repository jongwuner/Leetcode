class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heappush(pq, -stone)
        
        while len(pq) > 1:
            top1 = -heappop(pq)
            top2 = -heappop(pq)
            if top1 != top2:
                heappush(pq, -(top1 - top2))
        
        if len(pq) > 0:
            return -pq[0]
        else:
            return 0