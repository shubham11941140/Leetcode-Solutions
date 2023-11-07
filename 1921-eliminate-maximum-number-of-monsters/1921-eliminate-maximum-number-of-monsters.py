class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [math.ceil(d / s) for d, s in zip(dist, speed)]
        time.sort()
        for i in range(len(time)):
            if i >= time[i]:
                return i
        return len(time)        