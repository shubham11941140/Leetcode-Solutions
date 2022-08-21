class Solution:          
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [10 ** 10 for i in range(amount + 1)]
        arr[0] = 0
        for j in range(amount + 1):
            for i in coins:                        
                if j >= i:
                    arr[j] = min(arr[j], arr[j - i] + 1)
        return -1 if arr[amount] == 10 ** 10 else arr[amount]
        
