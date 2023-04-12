class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace("//", "/")
        chunks = path.split('/')
        cnt = 0
        ansPath = ""
        for i in range(len(chunks)-1, 0, -1):
            if chunks[i] == '..':
                cnt += 1
            elif chunks[i] == '.':
                pass
            elif chunks[i] == '':
                if i == 0: 
                    ansPath = '/' + ansPath
            elif cnt > 0:
                cnt -= 1
            else:
                ansPath = '/' + chunks[i] + ansPath
        if ansPath == "":
            ansPath = '/'
        return ansPath