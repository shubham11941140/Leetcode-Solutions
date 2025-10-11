class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:     
        cnt = Counter(power)
        arr = sorted(cnt.keys())
        n = len(arr)
        dp = [0]*n
        for i in range(n):
            val = arr[i] * cnt[arr[i]]
            j = i - 1
            while j>=0 and arr[i]-arr[j]<=2:
                j -= 1
            dp[i] = max(dp[i - 1] if i else 0, val + (dp[j] if j >= 0 else 0))
        return dp[-1]      