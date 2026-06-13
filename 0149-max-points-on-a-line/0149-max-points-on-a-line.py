class Solution:

    def slope(self, p1, p2):
        return "inf" if p1[0] == p2[0] else (p1[1] - p2[1]) / (p1[0] - p2[0])

    def maxPoints(self, p: List[List[int]]) -> int:
        n = len(p)
        if n < 3:
            return n
        mp = 0
        for i in range(n):
            sd = {}
            sp = 1
            for j in range(i + 1, n):
                if p[i][0] == p[j][0] and p[i][1] == p[j][1]:
                    sp += 1
                    continue
                s = self.slope(p[i], p[j])
                sd[s] = sd[s] + 1 if s in sd else 1
            mp = max(mp, sp + max(sd.values()) if sd else sp)
        return mp
