class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        self.s = []
        for _ in range(300):
            s = []
            if self.s:
                asteroids = self.s[-1].copy()
            for i in asteroids:
                if not s:
                    s.append(i)
                    continue
                if s[-1] > 0 and i < 0:
                    if s[-1] == abs(i):
                        s.pop()
                    elif s[-1] < abs(i):
                        s[-1] = i                                          
                else:
                    s.append(i)
            if s == asteroids:
                return s
            else:
                asteroids = s
            