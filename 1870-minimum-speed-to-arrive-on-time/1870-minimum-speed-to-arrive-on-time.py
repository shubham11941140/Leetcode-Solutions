class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        @cache
        def check(s):
            return sum([ceil(dist[i] / s) for i in range(n - 1)]) + (dist[-1] / s) <= hour        
        left, right = 1, 10**7        
        while left < right:
            mid = (left + right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid + 1        
        return left if check(left) else -1        