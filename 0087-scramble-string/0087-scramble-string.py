class Solution:
    def __init__(self):
        self.map = {}
        
    def StrSlice(self, leftStr, rightStr, flag):
        left = Counter()
        right = Counter()

        for c in leftStr:
            left[c] += 1
        for c in rightStr:
            right[c] += 1

        if flag == False : return left    
        if flag == True  : return right

    def getAnswer(self, s1, s2):
        if (s1, s2) in self.map:
            return self.map[(s1, s2)]

        if s1 == s2:
            self.map[(s1, s2)] = True
            return True

        N = len(s1)
        if len(s2) != N:
            self.map[(s1, s2)] = False
            return False

        for i in range(1,N): # 자르는 위치

            # left : False / right : True
            s1LeftSet = self.StrSlice(s1[:i], s1[i:], False)
            s2LeftSet_Non = self.StrSlice(s2[:i], s2[i:], False)
            s2RightSet_Swap = self.StrSlice(s2[:-i], s2[-i:], True)

            if s1LeftSet == s2LeftSet_Non:
                if self.getAnswer(s1[:i], s2[:i]) and self.getAnswer(s1[i:], s2[i:]):
                    return True
            if s1LeftSet == s2RightSet_Swap:
                if self.getAnswer(s1[:i], s2[-i:]) and self.getAnswer(s1[i:], s2[:-i]):
                    return True

        self.map[(s1, s2)] = False
        return False

    def isScramble(self, s1: str, s2: str) -> bool:
        return self.getAnswer(s1, s2)
