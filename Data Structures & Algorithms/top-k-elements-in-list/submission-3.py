class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        for i in nums:
            f[i] = 1 + f.get(i, 0)
        f = sorted(f.items(), key=lambda x: x[1])
        out = []
        for i in range(k):
            out.append(f.pop()[0])
        return out
