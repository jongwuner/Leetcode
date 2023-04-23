class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        def getAnswer(s, dp, start, end, k):
            if s[start] == '0':
                dp[start] = 0
                return 0
            if start == end - 1:
                dp[start] = 1
                return 1
            if dp[start] != -1:
                return dp[start]
            
    
            num = int(s[start])
            ans = 0
            for i in range(start + 1, end):
                if num > k: 
                    break
                ans = int((ans + getAnswer(s, dp, i, N, k)) % (1e9 + 7))
                num = num * 10 + int(s[i])
            if num <= k:
                ans += 1
            dp[start] = ans
            return dp[start]
            
        N = len(s)
        dp = [-1 for _ in range(N)]
        getAnswer(s, dp, 0, N, k)
        return dp[0]
        