class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        p = [-1] * n
        idxOrigin = {}
        idxCounter = defaultdict(list)
        
        def find(n):
            if p[n] < 0: return n
            p[n] = find(p[n])
            return p[n]
        
        def merge(a, b):
            a = find(a)
            b = find(b)
            if a == b: return
            p[a] += p[b]
            p[b] = a
        
        N = len(edgeList)
        M = len(queries)
        edgeIdx = 0
        ans = [0] * M
        
        
        for i, query in enumerate(queries):
            idxOrigin[tuple(query)] = i
            idxCounter[tuple(query)].append(i)
        
        edgeList = sorted(edgeList, key=lambda edgeList: edgeList[2])
        tmpQueries = sorted(queries, key=lambda queries: queries[2])
        
        for query in tmpQueries:
            fromNode = query[0]
            toNode = query[1]
            maxDis = query[2]
            
            while edgeIdx < N and edgeList[edgeIdx][2] < maxDis:
                merge(edgeList[edgeIdx][0], edgeList[edgeIdx][1])
                edgeIdx += 1
                
            idx = idxOrigin[(tuple(query))]
            isAnswer = True if find(toNode) == find(fromNode) else False
            if len(idxCounter[tuple(query)]) == 1:
                ans[idx] = isAnswer
            else:
                for nowIdx in idxCounter[tuple(query)]:
                    ans[nowIdx] = isAnswer
        return ans