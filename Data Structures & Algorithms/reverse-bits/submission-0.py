class Solution:
    def reverseBits(self, n: int) -> int:
        total = 0
        i = 31
        while n != 0:
            if n % 2 != 0:
                total += 2 ** i
            n //= 2
            i -= 1
        return total