class Solution:
    def addBinary(self, a: str, b: str) -> str:
        out = ""
        carry = 0
        while len(a) < len(b):
            a = '0' + a
        while len(b) < len(a):
            b = '0' + b
        for i in range(len(a)-1, -1, -1):
            if a[i] == '1' and b[i] == '1' and carry == 0:
                out = '0' + out
                carry = 1
            elif a[i] == '1' and b[i] == '1' and carry == 1:
                out = '1' + out
                carry = 1
            elif a[i] == '1' and b[i] == '0' and carry == 0:
                out = '1' + out
                carry = 0
            elif a[i] == '1' and b[i] == '0' and carry == 1:
                out = '0' + out
                carry = 1
            elif a[i] == '0' and b[i] == '1' and carry == 0:
                out = '1' + out
                carry = 0
            elif a[i] == '0' and b[i] == '1' and carry == 1:
                out = '0' + out
                carry = 1
            elif a[i] == '0' and b[i] == '0' and carry == 0:
                out = '0' + out
                carry = 0
            elif a[i] == '0' and b[i] == '0' and carry == 1:
                out = '1' + out
                carry = 0
            else:
                pass
        if carry == 1:
            out = '1' + out
        return out