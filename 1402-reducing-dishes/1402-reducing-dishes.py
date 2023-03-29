class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction = sorted(satisfaction, reverse=True)
        N = len(satisfaction)

        ans = 0

        for i in range(0, N):
            sum = 0
            for j in range(1, i+2):
                sum += satisfaction[i + 1 - j] * j
            ans = max(ans, sum)

        return ans