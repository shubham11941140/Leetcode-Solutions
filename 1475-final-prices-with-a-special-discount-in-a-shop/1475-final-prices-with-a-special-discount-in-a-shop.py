class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        final_prices = prices[:]
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    final_prices[i] = prices[i] - prices[j]
                    break
        return final_prices     