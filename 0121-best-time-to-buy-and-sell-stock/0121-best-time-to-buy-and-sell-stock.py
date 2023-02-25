class Solution(object):
    def maxProfit(self, prices):
        dp = list()
        N = prices.__len__()
        minVal = 10000000
        for i in range(N):
            minVal = min(prices[i], minVal)
            dp.append(prices[i] - minVal)

        return max(dp)