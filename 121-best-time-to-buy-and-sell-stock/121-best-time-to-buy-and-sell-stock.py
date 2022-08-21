class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        msf = [0 for i in range(n)]
        msf[0] = prices[0]
        for i in range(1, n):
            msf[i] = min(msf[i - 1], prices[i])
        ans = -1
        for i in range(n):
            ans = max(ans, prices[i] - msf[i])
        return ans
            
        
