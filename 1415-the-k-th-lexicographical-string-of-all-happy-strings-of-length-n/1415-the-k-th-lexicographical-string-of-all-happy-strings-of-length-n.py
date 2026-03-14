from itertools import product

class Solution:
    def getHappyString(self, n: int, k: int) -> str:        
        # Generate all happy strings of length n
        def ishappy(s):
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    return False
            return True
        h = sorted([''.join(p) for p in product('abc', repeat = n) if ishappy(''.join(p))])
        # Return the k-th happy string if it exists
        return h[k - 1] if k <= len(h) else ""      