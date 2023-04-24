### 문제정의
- 해당 리스트에서 문제 조건에 맞게 돌을 없애고, 돌의 가중치를 줄이는 규칙을 적용해서, 최후에 남는 돌의 value를 반환하라. 최후의 남는 돌이 없을 때는 0을 반환하라. 
### 솔루션
- O(NlogN). PQ. maxHeap으로 사용해서, pop1, pop2을 계속 줄여나가다가 보면, 최후의 pq값에 들어있는 값을 반환한다.  
### 기록
- from heapq import heappush, heappop / heappush(pq, element) / heappop(pq)
### 접근과정
- X
