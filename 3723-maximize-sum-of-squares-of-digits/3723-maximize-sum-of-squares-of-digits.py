class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        return "" if sum > 9 * num else ("9" * (sum // 9) + str(sum % 9) + "0" * num)[:num]