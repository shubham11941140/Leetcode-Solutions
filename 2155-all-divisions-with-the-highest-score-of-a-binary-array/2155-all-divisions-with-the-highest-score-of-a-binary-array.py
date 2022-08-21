class Solution:

    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        rone = nums.count(1)
        lzero = 0
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[i] = rone + lzero
            if not nums[i]:
                lzero += 1
            else:
                rone -= 1
        a.append(lzero + rone)
        m = max(a)
        return [i for i in range(len(a)) if a[i] == m]
