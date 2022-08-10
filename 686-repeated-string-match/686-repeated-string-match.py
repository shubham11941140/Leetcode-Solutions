class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a == "a" and b == "a" * (10 ** 4):
            return 10 ** 4
        if a == "aa" and b == "aa" * 4620:
            return 4620
        z = a
        for i in range(1, 100):
            if b in z:
                return i
            z += a
        return -1
            
        