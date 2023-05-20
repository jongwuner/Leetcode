from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        # Build the graph from equations
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val
        
        def dfs(s, e, path):
            # Found the target node
            if s == e:
                return path
            visited.add(s)
            for neighbor in graph[s]:
                if neighbor not in visited:
                    temp = dfs(neighbor, e, path * graph[s][neighbor])
                    if temp:
                        return temp
            return None

        results = []
        for s, e in queries:
            visited = set()
            if s not in graph or e not in graph:
                results.append(-1.0)
            else:
                res = dfs(s, e, 1.0)
                if res:
                    results.append(res)
                else:
                    results.append(-1.0)

        return results
