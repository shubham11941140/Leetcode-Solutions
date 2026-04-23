class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = sorted([math.ceil(d / s) for d, s in zip(dist, speed)])
        for i in range(len(time)):
            if i >= time[i]:
                return i
        return len(time)
