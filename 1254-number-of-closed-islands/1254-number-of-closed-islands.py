class Solution:
    def __init__(self):
        self.visited = set()
        self.N = 0
        self.M = 0
        self.isClosed = True
        
    def DFS(self, grid, row, col):
        mvY = [1, 0, -1, 0]
        mvX = [0, -1, 0, 1]

        self.visited.add((row, col))
        for k in range(4):
            nextY = row + mvY[k]
            nextX = col + mvX[k]

            if 0 > nextY or nextY > self.N - 1 or 0 > nextX or nextX > self.M - 1:
                self.isClosed = False
                continue 
            if grid[nextY][nextX] != 0:
                continue
            if (nextY, nextX) in self.visited:
                continue

            self.DFS(grid, nextY, nextX)
            
    def closedIsland(self, grid: List[List[int]]) -> int:
        area = []

        ans = 0 
        self.N = len(grid)
        self.M = len(grid[0])

        for i in range(self.N):
            for j in range(self.M):
                if grid[i][j] == 0 and (i, j) not in self.visited:
                    self.isClosed = True
                    self.DFS(grid, i, j)
                    if self.isClosed == True:
                        ans += 1

        return ans
