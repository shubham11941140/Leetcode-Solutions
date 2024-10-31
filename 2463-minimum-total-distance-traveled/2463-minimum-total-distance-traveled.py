class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        fp = [f[0] for f in factory]
        fl = [f[1] for f in factory]
        
        # Memoized recursive function
        @lru_cache(None)
        def dp(ri: int, fi: int) -> int:
            if ri == len(robot):
                return 0
            if fi == len(fp):
                return float('inf')
            m = dp(ri, fi + 1)
            t = 0
            for i in range(fl[fi]):
                if ri + i < len(robot):
                    t += abs(robot[ri + i] - fp[fi])
                    m = min(m, t + dp(ri + i + 1, fi + 1))
                else:
                    break            
            return m
        return dp(0, 0)        