class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        min_step = max(abs(sx - fx), abs(sy - fy))
        return t != 1 if not min_step else min_step <= t
