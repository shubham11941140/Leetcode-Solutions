class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        b = [i for i in nums if -i in nums]
        return max(b) if b else -1
                
        