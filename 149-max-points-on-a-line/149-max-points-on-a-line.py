class Solution:

    @staticmethod
    def equ(p1, p2):
        n = p1[1] - p2[1]
        d = p1[0] - p2[0]
        if d == 0:
            return 10**15, 10**15
        a = n / d
        c = p1[1] - (a * p1[0])
        return a, c

    @staticmethod
    def lies(a, c, p):
        return abs(p[1] - (a * p[0] + c)) < 10**(-5)

    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2:
            return 1
        ans = -1
        for i in range(n):
            for j in range(i + 1, n):
                a, c = self.equ(points[i], points[j])
                cp = 0
                for k in range(n):
                    if a == 10**15:
                        if points[j][0] == points[k][0]:
                            cp += 1
                    elif self.lies(a, c, points[k]):
                        cp += 1
                ans = max(ans, cp)
        return ans
