class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        f = {}
        for c in s:
            if c in f:
                f[c] += 1
            else:
                f[c] = 1
        for c in t:
            if c in f:
                f[c] -= 1
            else:
                return False
        for c in f.values():
            if c != 0:
                return False
        return True