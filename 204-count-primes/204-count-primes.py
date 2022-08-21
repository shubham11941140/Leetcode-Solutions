from math import ceil, sqrt

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        prime = [False] * (n + 1)
        prime[0] = True
        prime[1] = True
        for p in range(2, ceil(sqrt(n)) + 1):
            if not prime[p]:
                for j in range(p*p, n + 1, p):
                    prime[j] = True
        return len([i for i in range(n) if not prime[i]])
        
