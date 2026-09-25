class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = dict()
        for i in nums:
            m[i] = 1 + m.get(i, 0)
        for i in m:
            if m[i] == 1:
                return i