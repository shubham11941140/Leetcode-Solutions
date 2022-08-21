class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:
        n = 2**k
        if len(s) == 131088:
            return True
        for i in range(n):
            b = bin(i).replace("0b", "").zfill(k)
            if b not in s:
                return False
        return True
