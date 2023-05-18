class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reachable = [False]*n
        for edge in edges:
            reachable[edge[1]] = True
        return [i for i in range(n) if not reachable[i]]
