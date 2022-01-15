from collections import Counter

class Solution:
    def minJumps(self, arr: List[int]) -> int:        
        n = len(arr)
        MAX = 10 ** 10
        dp = [MAX for i in range(n)]        
        dp[0] = 0
        d = Counter(arr)
        for i in d:
            d[i] = MAX
        d[arr[0]] = 0
        ans = MAX        
        while True:
            changed = dp.copy()
            for i in range(1, n):            
                dp[i] = min(dp[i - 1], dp[i + 1] if i < n - 1 else MAX, d[arr[i]]) + 1
                d[arr[i]] = min(dp[i], d[arr[i]])
            ans = min(ans, dp[n - 1])
            if dp == changed:
                break
        return ans
        