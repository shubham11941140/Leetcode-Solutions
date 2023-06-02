class Solution:
    
    def dist(self, cod1, cod2):
        return math.sqrt(math.pow(cod1[0] - cod2[0], 2) + math.pow(cod1[1] - cod2[1], 2))    
    
    def dfs(self, curr, d):
        d.add(curr)
        for i in self.u: 
            if i not in d:
                if self.dist(curr, i) <= curr[2]:  
                    self.dfs(i, d)
    
    def maximumDetonation(self, bombs: List[List[int]]) -> int:   
        nb = [(i[0], i[1], i[2]) for i in bombs]
        self.u = nb.copy()
        c = Counter(nb)
        #print(nb)
        m = []
        for i in nb:
            d = set()
            self.dfs(i, d)
            s = len(d)
            s += sum([c[i] - 1 for i in d])
            m.append(s)
        return max(m)

       