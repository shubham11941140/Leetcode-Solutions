class Solution:

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        s = 0
        m = [0] * k
        for i in nums:
            s += i
            m[s % k] += 1
        c = m[0]
        for i in m:
            if i > 1:
                c += (i * (i - 1)) // 2
        return c
