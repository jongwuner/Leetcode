class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        dx, dy = 0, 1
        x, y = 0, 0
        for i in range(1, n*n+1):
            matrix[x][y] = i
            if not(0 <= x+dx < n and 0 <= y+dy < n and matrix[x+dx][y+dy] == 0):
                dx, dy = dy, -dx
            x += dx
            y += dy
        return matrix