class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = max(nums)
        if len(nums) != m + 1:
            return False
        nums.sort()
        print(nums)
        j = 1
        for i in range(m):
            if nums[i] != j:
                return False
            j += 1
        return nums[-1] == m

        