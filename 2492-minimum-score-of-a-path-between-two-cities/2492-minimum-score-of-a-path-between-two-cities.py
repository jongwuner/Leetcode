class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        global visited, isAnswerGraph, ans
        visited = set()
        ans = 10**5

        def dfs(curr):
            global isAnswerGraph, visited, ans

            val = 10**5
            if curr == 1:
                isAnswerGraph = True
            visited.add(curr)
            for next in graph[curr]:
                ans = min(ans, next[1])
                if next[0] in visited: 
                    continue
                dfs(next[0])


        graph = [[] for _ in range(n+1)]
        for i in range (len(roads)):
            s = roads[i][0]
            e = roads[i][1]
            wei = roads[i][2]

            graph[s].append((e, wei))
            graph[e].append((s, wei))

        for i in range (1, n + 1):
            isAnswerGraph = False
            if not i in visited:
                dfs(i)
                if isAnswerGraph == True:
                    return ans