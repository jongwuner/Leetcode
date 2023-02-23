import heapq
from heapq import heappop

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        N = profits.__len__()

        minHeap_capital = []
        maxHeap_profits = []

        for i in range(N):
            heapq.heappush(minHeap_capital, [capital[i], i])

        while minHeap_capital.__len__() > 0 and k > 0:
            if minHeap_capital[0][0] <= w:
                idx = minHeap_capital[0][1]
                heapq.heappush(maxHeap_profits, -profits[idx])
                heappop(minHeap_capital)
            elif maxHeap_profits.__len__() > 0:
                w += -heappop(maxHeap_profits)
                k -= 1
            else:
                break

        while k > 0 and maxHeap_profits.__len__() > 0:
            w += -heappop(maxHeap_profits)
            k -= 1

        return w