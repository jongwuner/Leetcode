class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n - 1 > len(connections):
            return -1

        global visited, graph

        def dfs(curr):
            global visited, graph
            visited.add(curr)
            for next in graph[curr]:
                if next in visited:
                    continue
                dfs(next)

        cnt = 0
        visited = set()

        graph = [[] for _ in range(n)]
        for edge in connections:
            s = edge[0]
            e = edge[1]
            graph[s].append(e)
            graph[e].append(s)

        for i in range (n):
            if not i in visited:
                dfs(i)
                cnt += 1

        return cnt - 1