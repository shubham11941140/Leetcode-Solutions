class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        remainder = n % 7

        total = 0
        for i in range(weeks):
            total += sum(range(i + 1, i + 8))

        total += sum(range(weeks + 1, weeks + 1 + remainder))

        return total
