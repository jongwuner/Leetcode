class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        global visited, finished, ans

        ans = -1
        visited = [-1] * (10**5)
        finished = [-1] * (10**5)

        def DFS(curr, edges, times):
            global visited, finished, ans

            visited[curr] = times
            next = edges[curr]
            if next == -1:
                finished[curr] = 1
                return
            if visited[next] == -1:
                DFS(next, edges, times + 1)
            elif finished[next] == -1:
                ans = max(ans, visited[curr] - visited[next] + 1)
            finished[curr] = 1

        for i in range (len(edges)):
            if visited[i] != -1:
                continue
            DFS(i, edges, 0)
    
        return ans