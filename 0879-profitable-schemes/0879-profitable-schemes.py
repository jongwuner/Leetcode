class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):

        m = len(group)
        f = [[0] * (minProfit + 1) for _ in range(n + 1)]
        f[0][0] = 1
        mod = 10**9 + 7
        for cost, w in zip(group, profit):
            for i in range(n - cost, -1, -1):
                for j in range(minProfit, -1, -1):
                    if j + w >= minProfit:
                        f[i + cost][minProfit] = (f[i + cost][minProfit] + f[i][j]) % mod
                    else:
                        f[i + cost][j + w] = (f[i + cost][j + w] + f[i][j]) % mod
        
        res = 0
        for i in range(n + 1):
            res = (res + f[i][-1]) % mod
        return res