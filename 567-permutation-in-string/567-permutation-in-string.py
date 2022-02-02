class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        s1 = sorted(list(s1))
        for i in reversed(range(n)):
            if sorted(s2[i:i + k]) == s1:
                return True
        return False
        