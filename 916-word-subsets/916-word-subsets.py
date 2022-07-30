from collections import Counter

class Solution:
        
    def comp(self, a, b):      
        for i in b:
            if i not in a:
                return False
            elif b[i] > a[i]:
                return False
        return True
        
    def union(self, d1, d2):        
        for i in d2:
            d1[i] = d2[i] if i not in d1 else max(d1[i], d2[i])                                    
        return d1
    
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        w1 = [Counter(i) for i in words1]
        w2 = [Counter(i) for i in words2]        
        d = dict()
        m = len(w1)
        for j in w2:
            d = self.union(d, j)                
        return [words1[i] for i in range(m) if self.comp(w1[i], d)]                  