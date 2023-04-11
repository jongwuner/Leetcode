class Solution:
    def removeStars(self, s: str) -> str:
        ans = ""
        cnt = 0
        i = len(s) - 1
        while i >= 0:
            if s[i] == '*':
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                ans = s[i] + ans
            i -= 1
        return ans
        

sol = Solution()
ans = sol.removeStars("leet**cod*e")
print(ans)