class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        def check(x1, y1, x2, y2):
            return ps[x2][y2] - ps[x1][y2] - ps[x2][y1] + ps[x1][y1] > 0

        def mem(k, i, j):
            tmp = 0
            for t in range(i + 1, row + 1):
                if check(i, j, t, col):
                    if dp[k - 1][t][j] == -1:
                        mem(k - 1, t, j)
                    tmp += dp[k-1][t][j]
            for t in range(j + 1, col + 1):
                if check(i, j, row, t):
                    if dp[k - 1][i][t] == -1:
                        mem(k - 1, i, t)
                    tmp += dp[k - 1][i][t]
            tmp = tmp % 1000000007
            dp[k][i][j] = tmp
            return tmp
        
        row, col = len(pizza), len(pizza[0])
        ps = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + int(pizza[i - 1][j - 1] == 'A')
        if k == 1:
            return int(check(0,0,row,col))
        dp = [[[-1] * (col + 1) for i in range(row + 1)] for j in range(k)]
        for i in range(row + 1):
            for j in range(col + 1):
                dp[0][i][j] = int(check(i, j, row, col))
        return mem(k-1, 0, 0)