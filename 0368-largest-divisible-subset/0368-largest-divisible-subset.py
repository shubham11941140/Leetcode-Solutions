class Solution:

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        solution = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(
                        solution[i]) < len(solution[j]) + 1:
                    solution[i] = solution[j] + [nums[i]]
        return max(solution, key=len)
