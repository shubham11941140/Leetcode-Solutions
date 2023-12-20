class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Sort the prices array in ascending order
        prices.sort()

        # Calculate the cost of the two cheapest chocolates
        cost = prices[0] + prices[1]

        # Check if you can afford to buy the two chocolates without going into debt
        if cost <= money:
            # If you can afford, return the leftover amount
            return money - cost
        else:
            # If you cannot afford, return the initial amount of money
            return money        