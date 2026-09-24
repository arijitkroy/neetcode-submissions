class Solution:
    def countBits(self, n: int) -> List[int]:
        count = []
        for i in range(n + 1):
            c = 0
            while i != 0:
                if i % 2 != 0:
                    c += 1
                i //= 2
            count.append(c)
        return count   