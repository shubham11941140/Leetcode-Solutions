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
                # Check sign of s[-1] and i
                # If both have same sign proceeed

                print(s[-1], i)
                if s[-1] > 0 and i < 0:
                    # Do nonsense
                    if s[-1] == abs(i):
                        s.pop()
                        continue
                    elif s[-1] < abs(i):
                        s.pop()
                        s.append(i)
                        continue
                    elif s[-1] > abs(i):
                        continue
                else:
                    s.append(i)
                    continue
            self.s.append(s)
            if len(self.s) > 2 and self.s[-2] == self.s[-1]:
                break
        return self.s[-1]
