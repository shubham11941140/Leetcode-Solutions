class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        r = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while s and temperatures[s[-1]] < t:
                idx = s.pop()
                r[idx] = i - idx
            s.append(i)
        return r        