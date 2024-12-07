class Solution:

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if sum([(num - 1) // mid for num in nums if num > mid]) <= maxOperations:
                right = mid
            else:
                left = mid + 1
        return left
