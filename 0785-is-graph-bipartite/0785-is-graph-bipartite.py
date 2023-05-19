
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        
        for i in range(n):
            if color[i] == -1:
                queue = [i]
                color[i] = 1
                
                while queue:
                    node = queue.pop(0)
                    
                    for neighbor in graph[node]:
                        if color[neighbor] == -1:
                            queue.append(neighbor)
                            color[neighbor] = 1 - color[node]
                        elif color[neighbor] == color[node]:
                            return False
        return True
