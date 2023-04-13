class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = deque()
        hash = {}
        for i, key in enumerate(pushed):
            hash[key] = i
        maxVal = -1
        pushIdx = 0
        for i, key in enumerate(popped):
            top = -1 if len(st) == 0 else st[-1]
            if maxVal < hash[key]:
                maxVal = hash[key]
                while(len(st) >= 0 and pushIdx < len(pushed) and hash[key] != top):
                    st.append(hash[pushed[pushIdx]])
                    pushIdx += 1
                    top = st[-1]
                if len(st) >= 0 and pushIdx < len(pushed) and hash[key] != top:
                    return False
                st.pop()
            else:
                if hash[key] != top:
                    return False
                st.pop()
        if len(st) > 0:
            return False
        return True