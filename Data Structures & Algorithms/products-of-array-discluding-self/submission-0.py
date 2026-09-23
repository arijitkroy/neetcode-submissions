class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) >= 2:
            return [0] * len(nums)
        prod = 1
        for i in nums:
            if i != 0:
                prod *= i
        out = []
        if nums.count(0) == 0:
            for i in nums:
                out.append(prod // i)
        else:
            for i in nums:
                if i == 0:
                    out.append(prod)
                else:
                    out.append(0)
        return out