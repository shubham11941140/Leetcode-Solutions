from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        sm = Counter(s1)
        for i in reversed(range(n)):
            if Counter(s2[i:i + k]) == sm:
                return True
        return False
        
