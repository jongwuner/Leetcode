class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        nowCnt = 0
        for i, chr in enumerate(s):
            if chr == 'a' or chr == 'e' or chr == 'i' or chr == 'o' or chr == 'u':
                nowCnt += 1
            if i < k:
                ans = max(ans, nowCnt)
            else:
                if s[i - k] == 'a' or s[i - k] == 'e' or s[i - k] == 'i' or s[i - k] == 'o' or s[i - k] == 'u':
                    nowCnt -= 1
                ans = max(ans, nowCnt)
        return ans