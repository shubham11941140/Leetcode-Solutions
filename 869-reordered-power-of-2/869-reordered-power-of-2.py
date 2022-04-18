from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for i in range(30):
            if Counter([y for y in str(n)]) == Counter([x for x in str(2 ** i)]):
                return True
        return False
        