class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        t = minutesToTest // minutesToDie
        print(t)
        print(t + 1, buckets)
        z = t + 1
        for i in range(100):
            if pow(z, i) >= buckets:
                return i
            
        