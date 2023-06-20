class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + nums[i]
        r = [-1] * n
        for i in range(k, n - k): 
            r[i] = (p[i + k + 1] - p[i - k]) // (2 * k + 1)
        return r