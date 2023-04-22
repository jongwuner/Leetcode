class Solution:
    def minInsertions(self, s: str) -> int:
        N = len(s)
        dp = [[0 for j in range(N)] for i in range(N)]
        for i in range(N):
            for j in range(N):
                if i > j: continue
                dp[i][j] = 5000
        
        for k in range(N):
            for i in range(N):
                if k == 0:
                    dp[i][i] = 0
                    continue
                if i + k >= N: 
                    continue
                tmp = min(dp[i][i] + k,  1 + dp[i + 1][i + k], dp[i][i + k - 1] + 1, k + dp[i + k][i + k])
                dp[i][i + k] = min(dp[i][i + k], tmp)
                # for h in range(k):
                #    tmp = min(dp[i][i + h] + (i + k) - (i + h + 1) + 1, (i + h) - i + 1 + dp[i + h + 1][i + k])
                #    dp[i][i + k] = min(dp[i][i + k], tmp)
                if s[i] == s[i + k]:
                    dp[i][i + k] = min(dp[i][i + k], dp[i + 1][i + k - 1])
        return dp[0][N - 1]