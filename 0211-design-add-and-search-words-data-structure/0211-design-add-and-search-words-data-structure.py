class WordDictionary:
    def __init__(self):
        self.wordDict = collections.defaultdict(list)
        

    def addWord(self, word):
        if len(word) in self.wordDict:
            self.wordDict[len(word)].append(word)
        else:
            self.wordDict[len(word)] = [word]
        

    def search(self, word):
        if word == None:
            return False
        if '.' not in word:
            return word in self.wordDict[len(word)]
        for v in self.wordDict[len(word)]:
            for i, ch in enumerate(word):
                if v[i] != ch and ch != '.':
                    break
            else: 
                return True
        return False
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)