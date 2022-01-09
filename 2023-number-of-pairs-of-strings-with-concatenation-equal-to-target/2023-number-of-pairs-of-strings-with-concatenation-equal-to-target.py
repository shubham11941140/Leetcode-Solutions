class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(nums)
        c = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    if nums[i] + nums[j] == target:
                        c += 1
        return c
                    
        