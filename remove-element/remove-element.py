class Solution:

    @staticmethod
    def removeElement(nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
