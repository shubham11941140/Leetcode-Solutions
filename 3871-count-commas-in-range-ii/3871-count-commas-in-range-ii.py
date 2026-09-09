class Solution:
    def countCommas(self, n: int) -> int:
        return max(n - 999, 0) + max(n - 999999, 0) + max(n - 999999999, 0) + max(n - 999999999999, 0) + max(n - 999999999999999, 0)
        