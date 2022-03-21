from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        f = Counter(nums)
        ans = 0
        for i in f:
            if k - i in f:
                ans += min(f[i], f[k - i])
        return ans // 2
                
        