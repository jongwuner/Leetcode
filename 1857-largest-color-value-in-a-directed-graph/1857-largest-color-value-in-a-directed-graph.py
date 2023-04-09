class Solution:
    def __init__(self):
        self.N = None
        self.dp = None
        self.adj = None
        self.colors = None
        self.visited = None
        self.finished = None
        self.isCycle = False
        
    def DFS(self, v):
        if v in self.visited:
            if v in self.finished:
                return self.dp[v]
            else:
                self.isCycle = True
                return None
                

        self.visited.add(v)
        nowColor = []

        for next in self.adj[v]:
            nowColor.append(self.DFS(next))
        
        if self.isCycle == True:
            return None

        for i in range(len(nowColor)):
            for j in range(26):
                self.dp[v][j] = max(self.dp[v][j], nowColor[i][j])

        self.dp[v][ord(self.colors[v]) - ord('a')] += 1
        self.finished.add(v)

        return self.dp[v]
        
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        self.N = len(colors)
        self.dp = [[0 for j in range(26)] for i in range(self.N)]
        self.adj = [[] for i in range(self.N)]
        self.colors = colors
        
        for edge in edges:
            self.adj[edge[0]].append(edge[1])

        self.visited = set()
        self.finished = set()
        ans = 0

        for i in range(self.N):
            self.DFS(i)
            if self.isCycle == True:
                return -1
            for j in range(26):
                ans = max(ans, self.dp[i][j])

        return ans