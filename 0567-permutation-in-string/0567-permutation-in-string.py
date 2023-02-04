from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)        
        if n < k:
            return False
        s = defaultdict(int)
        d = defaultdict(int)        
        for c in string.ascii_lowercase:
            s[c] = 0
            d[c] = 0
        for i in range(k):
            s[s1[i]] += 1
            d[s2[i]] += 1
        #print(d, s)
        if d == s:
            return True
        for i in range(k, n):
            d[s2[i - k]] -= 1
            d[s2[i]] += 1
            #print(d, s)
            if d == s:
                return True
        return False
        