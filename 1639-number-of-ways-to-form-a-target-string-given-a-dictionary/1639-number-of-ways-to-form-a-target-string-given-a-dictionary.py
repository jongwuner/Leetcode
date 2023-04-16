class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        postoletter = collections.defaultdict(list)
        for i in range(len(words)):
            for j in range(len(words[i])):
                postoletter[j].append(words[i][j])
        indextoCounter = collections.defaultdict()
        for idx, lst in postoletter.items():
            indextoCounter[idx] = collections.Counter(lst)
        dp = [[0 for _ in range(len(target))] for _ in range(len(words[0]))]
        
        dp[0][0] = indextoCounter[0][target[0]]
        
        for i in range(1, len(words[0])):
            dp[i][0] = dp[i-1][0] + indextoCounter[i][target[0]]
            for j in range(1, min(i+1, len(target))):
                dp[i][j] = dp[i-1][j-1]* indextoCounter[i][target[j]]  + dp[i-1][j]
                
        return dp[-1][-1]%(10**9 + 7)