class Solution:

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        s = 0
        m = [0] * k
        for i in nums:
            s += i
            m[s % k] += 1
        return m[0] + sum([(i * (i - 1)) // 2 for i in m if i > 1])
