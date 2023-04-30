class Solution:
    def __init__(self):
        self.isCompleted = False
        self.adj = None
        self.visited = set()
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        self.adj = [[] for i in range(n + 1)]
        blueP = [-1] * (n + 1)
        blueMax = 0
        totalType = [0, 0, 0]
        ans = 0
        
        def find(n):
            if blueP[n] < 0: return n
            blueP[n] = find(blueP[n])
            return blueP[n]
        def merge(a, b):
            a = find(a)
            b = find(b)
            if a == b: return
            blueP[a] += blueP[b]
            blueP[b] = a
        def makeTree(type, nowNode):
            self.visited.add(nowNode)
            for next in self.adj[nowNode]:
                if next[1] != 3 and next[1] != type:
                    continue
                if next[0] in self.visited:
                    continue
                makeTree(type, nowNode = next[0])
        
        for edge in edges:
            a = edge[1]
            b = edge[2]
            type = edge[0]
            
            totalType[type - 1] += 1
            
            if type != 3:
                self.adj[a].append([b, type])
                self.adj[b].append([a, type])
            
            else :
                if find(a) != find(b):
                    blueMax += 1
                    merge(a, b)
                    self.adj[a].append([b, 3])
                    self.adj[b].append([a, 3])
        
        ans += (totalType[2] - blueMax)
        
        
        makeTree(type = 1, nowNode = 1)
        if len(self.visited) != n:
            return -1
        else:
            ans += (totalType[0] - (n - 1 - blueMax))
            
        self.visited.clear()
            
        makeTree(type = 2, nowNode = 1)
        if len(self.visited) != n:
            return -1
        else:
            ans += (totalType[1] - (n - 1 - blueMax))
        
        return ans