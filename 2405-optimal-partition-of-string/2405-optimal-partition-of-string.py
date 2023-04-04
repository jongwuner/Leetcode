class Solution:
    def partitionString(self, s: str) -> int:
        isChk = set()
        ans = 0
        for m in s:
            if m in isChk:
                ans += 1
                isChk.clear()
            isChk.add(m)
        ans += 1
        return ans