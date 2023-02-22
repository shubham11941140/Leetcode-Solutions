class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(weights, D, capacity):
            days = 1
            curr = 0
            for w in weights:
                if w > capacity:
                    return False
                if curr + w > capacity:
                    days += 1
                    curr = 0
                curr += w
            return days <= D

        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            if canShip(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        return left        