class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if sum([(q + mid - 1) // mid for q in quantities]) <= n:
                right = mid
            else:
                left = mid + 1
        return left        