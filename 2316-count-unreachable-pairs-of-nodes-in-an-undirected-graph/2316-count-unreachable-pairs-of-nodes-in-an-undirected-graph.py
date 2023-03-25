class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        global visited, graph, cnt

        ans = 0
        cnt = 0
        visited = set()
        graph = [[] for _ in range(n + 1)]


        def DFS(curr):
            global visited, graph, cnt

            visited.add(curr)    
            cnt += 1

            for next in graph[curr]:
                if next in visited:
                    continue
                DFS(next)

        for edge in edges:
            s = edge[0]
            e = edge[1]
            graph[s].append(e)
            graph[e].append(s)

        for num in range(n):
            if num in visited:
                continue
            cnt = 0
            DFS(num)
            ans += cnt * (n - len(visited))

        return ans
