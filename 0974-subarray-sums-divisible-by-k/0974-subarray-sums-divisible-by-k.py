class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        mod = [0] * k
        for i in range(len(nums)):
            sum += nums[i]
            mod[sum % k] += 1
        for i in range(k):
            if mod[i] > 1:
                count += (mod[i] * (mod[i] - 1)) // 2
        count += mod[0]
        return count        