from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return any(Counter([y for y in str(n)]) == Counter([x for x in str(2 ** i)]) for i in range(30))
        