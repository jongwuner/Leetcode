class Solution:
    def __init__(self):
        self.N = 0
        self.M = 0
        self.isClosed = True
        self.ans = 0
        self.cnt = 0
        self.visited = set()
        
        
    def DFS(self, grid, row, col):
        mvY = [1, 0, -1, 0]
        mvX = [0, -1, 0, 1]

        self.cnt += 1
        self.visited.add((row, col))
        for i in range(4):
            nextY = row + mvY[i]
            nextX = col + mvX[i]

            if nextY < 0 or nextY > self.N - 1 or nextX < 0 or nextX > self.M - 1:
                self.isClosed = False
                continue
            if grid[nextY][nextX] != 1:
                continue
            if (nextY, nextX) in self.visited:
                continue      
            self.DFS(grid, nextY, nextX)
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.N = len(grid)
        self.M = len(grid[0])
        
        for i in range(self.N):
            for j in range(self.M):
                if grid[i][j] == 1 and (i, j) not in self.visited:
                    self.isClosed = True
                    self.cnt = 0
                    self.DFS(grid, i, j)
                    if self.isClosed == True:
                        self.ans += self.cnt

        return self.ans