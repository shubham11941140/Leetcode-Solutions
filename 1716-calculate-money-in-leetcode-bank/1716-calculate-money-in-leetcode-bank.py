class Solution:
    def totalMoney(self, n: int) -> int:
        return sum([sum(range(i + 1, i + 8)) for i in range(n // 7)]) + sum(range((n // 7) + 1, (n // 7) + 1 + (n % 7)))     