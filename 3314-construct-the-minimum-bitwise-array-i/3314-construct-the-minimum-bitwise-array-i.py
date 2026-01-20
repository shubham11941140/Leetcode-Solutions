class Solution:

    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            ans.append(n - ((n + 1) & (-n - 1)) // 2 if n != 2 else -1)
        return ans
