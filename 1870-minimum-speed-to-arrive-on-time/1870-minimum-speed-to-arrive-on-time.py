class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        def check(speed):
            res = 0
            for i in range(n):
                res += (dist[i] / speed) if i == len(dist) - 1 else math.ceil(dist[i] / speed)
            return res <= hour
        
        left, right = 1, 10**7        
        while left < right:
            mid = (left + right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if check(left) else -1        