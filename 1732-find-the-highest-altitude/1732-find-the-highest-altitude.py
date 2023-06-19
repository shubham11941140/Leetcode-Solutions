class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = [0]
        c = 0
        m = 0
        for i in gain:
            c += i
            m = max(m, c)
            a.append(a[-1] + i)
        return m
        