class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        N = len(strs)
        M = len(strs[0])    
        p = [-1] * N
        groups = set()
        
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
            
        for i in range(0, N):
            for j in range(i + 1, N):
                cnt = 0
                for k in range(0, M):
                    if strs[i][k] != strs[j][k]:
                        cnt += 1
                if cnt <= 2:
                    merge(i, j)
        for i in range(N):
            groups.add(find(i))
        
        return len(groups)