import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) 
        heap = []
        for num, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            elif heap[0][0] < freq:
                heapq.heapreplace(heap, (freq, num))
        
        return [item[1] for item in heap]
