class Solution:

    @staticmethod
    def maximumUniqueSubarray(nums: List[int]) -> int:
        n = len(nums)
        pre = [0 for i in range(n)]
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + nums[i]
        l = 0
        r = 0
        a = set()
        ans = -1
        while r < n and l <= r:
            if nums[r] not in a:
                a.add(nums[r])
                r += 1
            elif nums[r] in a:
                a.remove(nums[l])
                l += 1
            ans = max(ans, pre[r - 1] - pre[l - 1] if l else pre[r - 1])
        return ans
