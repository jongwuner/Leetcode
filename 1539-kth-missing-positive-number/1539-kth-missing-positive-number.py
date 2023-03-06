class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = 0
        tcnt = 0
        idx = 0
        visited = [0] * 2500
        for i in range (len(arr)):
            visited[arr[i]] = True

        for i in range (1, 2500):
            if visited[i] == True:
                continue
            tcnt += 1
            ans = i
            if tcnt == k:
                break
        return ans
