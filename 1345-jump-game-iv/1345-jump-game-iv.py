class Solution:

    def freq(self, arr, MAX):
        d = {}
        for i in arr:
            if i not in d:
                d[i] = MAX
        return d

    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        MAX = 10**10
        dp = [MAX for i in range(n)]
        dp[0] = 0
        d = self.freq(arr, MAX)
        d[arr[0]] = 0
        ans = MAX
        while True:
            changed = dp.copy()
            for i in range(1, n):
                dp[i] = min(dp[i - 1], dp[i + 1] if i < n - 1 else MAX,
                            d[arr[i]]) + 1
                d[arr[i]] = min(dp[i], d[arr[i]])
            ans = min(ans, dp[n - 1])
            if dp == changed:
                break
        return ans
