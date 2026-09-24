class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t == '+':
                stk.append(stk.pop() + stk.pop())
            elif t == '*':
                stk.append(stk.pop() * stk.pop())
            elif t == '-':
                b, a = stk.pop(), stk.pop()
                stk.append(a - b)
            elif t == '/':
                b, a = stk.pop(), stk.pop()
                stk.append(int(float(a) / b))
            else:
                stk.append(int(t))
        return stk[-1]