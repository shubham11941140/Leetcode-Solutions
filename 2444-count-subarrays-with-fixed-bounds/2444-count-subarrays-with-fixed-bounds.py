class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        l = r = b = -1
        for i, num in enumerate(nums):
            if not minK <= num <= maxK:
                b = i
            if num == minK:
                l = i
            if num == maxK:
                r = i
            ans += max(0, min(l, r) - b)
        return ans