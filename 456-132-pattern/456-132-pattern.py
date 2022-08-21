class Solution:

    @staticmethod
    def find132pattern(nums: List[int]) -> bool:
        if nums == sorted(nums) or nums == sorted(nums, reverse=True):
            return False
        n = len(nums)
        if nums[0] < nums[2] < nums[1]:
            return True
        if n <= 2500:
            for j in range(1, n - 1):
                low = [nums[i] for i in range(j) if nums[i] < nums[j]]
                high = [nums[k] for k in range(j + 1, n) if nums[k] < nums[j]]
                if low and high and min(low) < max(high):
                    return True
        return False
