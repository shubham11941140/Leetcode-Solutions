class Solution:

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        c = 0
        s = 0
        m = [0] * k
        for i in range(len(nums)):
            s += nums[i]
            m[s % k] += 1
        for i in range(k):
            if m[i] > 1:
                c += (m[i] * (m[i] - 1)) // 2
        c += m[0]
        return c
