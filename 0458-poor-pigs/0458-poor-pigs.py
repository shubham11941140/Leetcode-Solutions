class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        t = (minutesToTest // minutesToDie) + 1
        for i in range(100):
            if t ** i >= buckets:
                return i
            
        