class Solution:

    @staticmethod
    def findKthLargest(nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]
