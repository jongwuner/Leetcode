class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        for mark in s:
            if mark == '(' or mark == '[' or mark == '{':
                st.append(mark)
            else:
                if len(st) == 0:
                    return False
                top = st.pop()
                if mark == ')' and top != '(':
                    return False
                elif mark == ']' and top != '[':
                    return False
                elif mark == '}' and top != '{':
                    return False
        if len(st) > 0:
            return False
        return True