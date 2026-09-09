class Solution:
    def countCommas(self, n: int) -> int:
        return sum([max(n - int(str(999) * i), 0) for i in range(1, 6)])
        return max(n - 999, 0) + max(n - 999999, 0) + max(n - 999999999, 0) + max(n - 999999999999, 0) + max(n - 999999999999999, 0)
        