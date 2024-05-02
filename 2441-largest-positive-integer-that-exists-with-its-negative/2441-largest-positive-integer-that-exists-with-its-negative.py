class Solution:

    def findMaxK(self, nums: List[int]) -> int:
        b = []
        for i in nums:
            if -i in nums:
                b.append(i)
        return max(b) if b else -1
