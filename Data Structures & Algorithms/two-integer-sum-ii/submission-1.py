class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = defaultdict(int)
        for i in range(len(numbers)):
            t = target - numbers[i]
            if m[t]:
                return [m[t], i+1]
            m[numbers[i]] = i + 1
        return []