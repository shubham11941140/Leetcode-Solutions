class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        q = deque()
        for i in range(len(nums)):
            if q and i - q[0] > k:
                q.popleft()
            dp[i] = nums[i] + (dp[q[0]] if q else 0)
            while q and dp[i] > dp[q[-1]]:
                q.pop()
            if dp[i] > 0:
                q.append(i)
        return max(dp)
