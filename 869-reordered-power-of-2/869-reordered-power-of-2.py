from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = [i for i in str(n)]
        cs = Counter(s)
        c = []
        for i in range(30):
            k = pow(2, i)
            t = [x for x in str(k)]
            if cs == Counter(t):
                return True
        return False
        
        print(2 ** 30 < 10 ** 9)
        