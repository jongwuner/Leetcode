from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            grid[i][j] = 2
            queue.append((i, j))
            for x, y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                    dfs(x, y)

        def bfs():
            steps = 0
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    for x, y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                        if 0 <= x < n and 0 <= y < n:
                            if grid[x][y] == 2:
                                continue
                            if grid[x][y] == 1:
                                return steps
                            grid[x][y] = 2
                            queue.append((x, y))
                steps += 1
            return 0
        
        n = len(grid)
        queue = deque()

        # Find the first island using DFS
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return bfs()
