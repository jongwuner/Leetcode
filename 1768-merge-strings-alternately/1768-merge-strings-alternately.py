class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        flg = True
        size = len(word1)
        if len(word1) > len(word2):
            size = len(word2)
            flg = False
            
        for i in range(size):
            ans += word1[i]
            ans += word2[i]
            
        if flg == True:
            for i in range(size, len(word2)):
                ans += word2[i]
        else:
            for i in range(size, len(word1)):
                ans += word1[i]
        return ans