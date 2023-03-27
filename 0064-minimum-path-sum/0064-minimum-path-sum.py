class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[0 for j in range(N)] for i in range(M)]
        for i in range(M):
            for j in range(N):
                if i - 1 < 0 and j - 1 < 0:
                    dp[i][j] = grid[i][j]
                elif i - 1 < 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j - 1 < 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[M - 1][N - 1]