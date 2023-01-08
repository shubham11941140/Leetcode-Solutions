class Solution:    
    def slope(self, p1, p2):
        return 'inf' if p1[0] == p2[0] else (p1[1] - p2[1]) / (p1[0] - p2[0])

    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return n
        mp = 0
        for i in range(n):
            sd = {}
            sp = 1
            for j in range(i + 1, n):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    sp += 1
                    continue
                s = self.slope(points[i], points[j])
                sd[s] = sd[s] + 1 if s in sd else 1
            mp = max(mp, sp + max(sd.values()) if sd else sp)
        return mp

                        
        