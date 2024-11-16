class Solution:
    
    def check(self, a):
        if max(a) - min(a) + 1 != len(a):
            return -1
        b = [i for i in range(min(a), max(a) + 1)]
        if a == b:
            return a[-1]
        else:
            return -1
    
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            v = self.check(subarray)
            power = sum(subarray) ** 2
            result.append(v)

        return result
        