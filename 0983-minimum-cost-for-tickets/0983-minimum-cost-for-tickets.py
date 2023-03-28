class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [9999999999] * 366
        idx = 0
        dp[0] = 0
        for i in range(1, 366):
            if i == days[idx]:
                if i >= 30:
                    dp[i] = min(dp[i - 1] + costs[0], dp[i - 7] + costs[1], dp[i - 30] + costs[2])
                elif i >= 7:
                    dp[i] = min(dp[i - 1] + costs[0], dp[i - 7] + costs[1], costs[2])
                elif i >= 1:
                    dp[i] = min(dp[i - 1] + costs[0], costs[1], costs[2])
                idx += 1
            elif i < days[idx]:
                if idx - 1 >= 0:
                    dp[i] = dp[days[idx - 1]]
                else:
                    dp[i] = dp[0]
                i += 1
            if idx >= len(days):
                break
        return dp[days[-1]]