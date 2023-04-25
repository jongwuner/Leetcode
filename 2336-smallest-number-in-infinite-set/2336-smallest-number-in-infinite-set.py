class SmallestInfiniteSet:
    def __init__(self):
        self.InifinitieSet = [True for _ in range(1, 1005)]

    def popSmallest(self) -> int:
        for i in range(1, 1005):
            if self.InifinitieSet[i] == True:
                self.InifinitieSet[i] = False
                return i

    def addBack(self, num: int) -> None:
        self.InifinitieSet[num] = True
        