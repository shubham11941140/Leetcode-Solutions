class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        last = {}       
        dp = [n] * n

        for i in range(n * 2):
            idx = i % n
            num = nums[idx]

            if num in last:
                prev = last[num]
                dist = i - prev

                dp[idx] = min(dp[idx], dist)
                dp[prev % n] = min(dp[prev % n], dist)

            last[num] = i

        return [-1 if dp[q] == n else dp[q] for q in queries]        