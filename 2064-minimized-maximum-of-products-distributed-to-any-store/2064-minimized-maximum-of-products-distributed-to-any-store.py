class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(mid):
            stores = 0
            for q in quantities:
                stores += (q + mid - 1) // mid
            return stores <= n

        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid
            else:
                left = mid + 1

        return left
        