### 문제정의
- n개의 정점과 정점 사이의 1개의 방향이 있는 간선만이 존재할 때, 모든 노드에서 0번 노드로 도달할 수 있도록, 에지의 방향을 바꿔야하는 최소 개수를 반환하라.
### 솔루션
- O(N), DFS 탐색. 간선 집합을 통해 유방향그래프(원본)와 무방향 그래프를 1개씩 만든다. 이후, 0에서 시작하는 DFS탐색을 해주면서 원본 유방향 그래프에서 다음 노드에서 현재 노드로 향하는 간선이 없을 때마다 카운트를 해준다.    
### 기록
- ![image](https://user-images.githubusercontent.com/16419202/227437981-f9d9be3d-f2a2-405a-bf57-89a6adf2529c.png)
  - class 내에서 전역변수를 썼는데, 왜 이게 오답이 나오지? ㅋㅋㅋ
  - global 쓰기 싫어서, 이거 한번 디버깅해봐야겠다. 
    ```python
    class Solution:
    visited = set()
    treeGraph = []
    originals = []
    ans = 0
    
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def treeOrder(self, curr):
            self.visited.add(curr)
            for next in self.treeGraph[curr]:
                if next in self.visited:
                    continue
                if next in self.originals[curr]:
                    self.ans += 1
                treeOrder(self,next)
    
        self.treeGraph = [[] for _ in range(n + 1)]
        self.originals = [[] for _ in range(n + 1)]

        for edge in connections:
            s = edge[0]
            e = edge[1]

            self.originals[s].append(e)
            self.treeGraph[s].append(e)
            self.treeGraph[e].append(s)    

        treeOrder(self,0)
        return self.ans

    ```
    - 인접노드에 부모노드도 있다면, 그것은 이미 트리가 아니다. 이거 명심할 것!!! 트리는 유방향 단방향이면서 사이클이 없고, n개에 정점에 대해 n-1 그래프다. 
### 접근과정
- 
