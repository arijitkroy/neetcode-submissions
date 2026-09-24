class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in ['(', '{', '[']:
                stk.append(c)
            if c == ')':
                if len(stk) == 0 or stk[-1] != '(':
                    return False
                stk.pop()
            if c == '}':
                if len(stk) == 0 or stk[-1] != '{':
                    return False
                stk.pop()
            if c == ']':
                if len(stk) == 0 or stk[-1] != '[':
                    return False
                stk.pop()
        return len(stk) == 0