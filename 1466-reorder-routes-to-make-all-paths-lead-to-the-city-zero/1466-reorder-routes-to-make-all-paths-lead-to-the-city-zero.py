class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        global visited, treeGraph, originals, ans

        ans = 0
        visited = set()

        def treeOrder(curr):
            global visited, treeGraph, originals, ans

            visited.add(curr)
            for next in treeGraph[curr]:
                if next in visited:
                    continue
                if next in originals[curr]:
                    ans += 1
                treeOrder(next)


        treeGraph = [[] for _ in range(n + 1)]
        originals = [[] for _ in range(n + 1)]
        for edge in connections:
            s = edge[0]
            e = edge[1]

            originals[s].append(e)
            treeGraph[s].append(e)
            treeGraph[e].append(s)    

        treeOrder(0)
        return ans
