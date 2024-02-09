class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        s = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if not (nums[i] % nums[j]) and len(s[i]) < len(s[j]) + 1:
                    s[i] = s[j] + [nums[i]]
        return max(s, key = len)        