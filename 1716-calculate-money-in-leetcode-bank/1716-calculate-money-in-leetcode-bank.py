class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        remainder = n % 7
        total = sum([sum(range(i + 1, i + 8)) for i in range(weeks)])
        total += sum(range(weeks + 1, weeks + 1 + (n % 7)))
        return total
