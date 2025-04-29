class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        if n % 3:
            return []
        nums = sorted(nums)
        ans = [nums[i * 3 : (i + 1) * 3] for i in range(n // 3)]
        return ans if all(max(x) - min(x) <= k for x in ans) else []
