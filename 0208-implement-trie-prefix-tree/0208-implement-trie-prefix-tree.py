class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curNode = self.root
        for c in word:
            if c not in curNode:
                curNode[c] = {}
            curNode = curNode[c]
        curNode['*'] = True

    def search(self, word: str) -> bool:
        curNode = self.root
        for c in word:
            if c not in curNode:
                return False
            curNode = curNode[c]
        return '*' in curNode 

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for c in prefix:
            if c not in curNode:
                return False
            curNode = curNode[c]
        return len(curNode) > 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)