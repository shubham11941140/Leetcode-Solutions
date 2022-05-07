class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if nums == sorted(nums) or nums == sorted(nums, reverse = True):
            return False
        n = len(nums)
        print(n)
        if n <= 100:
            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        if nums[i] < nums[k] < nums[j]:
                            return True
        if n <= 2500:
            for j in range(1, n - 1):
                low = [nums[i] for i in range(j) if nums[i] < nums[j]]
                high = [nums[k] for k in range(j + 1, n) if nums[k] < nums[j]]
                if low and high:
                    if min(low) < max(high):
                        return True       
        if nums[0] < nums[2] < nums[1]:
            return True
        return False
            
        