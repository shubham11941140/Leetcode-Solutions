class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        m = max(abs(sx - fx), abs(sy - fy))
        return t != 1 if not m else m <= t
