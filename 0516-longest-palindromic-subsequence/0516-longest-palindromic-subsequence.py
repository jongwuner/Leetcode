class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        DP = [[0 for j in range(N)] for i in range(N)]
        for i in range(N):
            DP[i][i] = 1
        for k in range(1, N):
            for i in range(N):
                if i + k >= N:
                    continue
                DP[i][i + k] = max(DP[i + 1][i + k], DP[i][i + k - 1])
                if s[i] == s[i + k]:
                    DP[i][i + k] = max(DP[i][i + k], DP[i + 1][i + k - 1] + 2)
        return DP[0][N - 1]