from collections import Counter

class Solution:
        
    def comp(self, a, b):      
        for i in b:
            if i not in a:
                return False
            else:
                if b[i] > a[i]:
                    return False
        return True
    
    
    def union(self, d1, d2):        
        for i in d2:
            if i not in d1:
                d1[i] = d2[i]
            else: # Present
                d1[i] = max(d1[i], d2[i])                                        
        return d1
    
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        w1 = [Counter(i) for i in words1]
        w2 = [Counter(i) for i in words2]
        
        d = dict()
        for j in w2:
            d = self.union(d, j)
        print(d)
        
        m = len(w1)
        ans = []
        for i in range(m):
            if self.comp(w1[i], d):
                print(words1[i])
                ans.append(words1[i])
        return ans
            
            
        
        
        
        
        n = len(w2)
        ans = []
        for j in w2:
            w = []
            c = []
            for i in range(len(w1)):
                if self.comp(w1[i], j):
                    w.append(words1[i])
                    c.append(w1[i])
            words1 = w.copy()
            w1 = c.copy()
        return words1                
            
                
        