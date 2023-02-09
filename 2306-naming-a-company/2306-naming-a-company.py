class Solution:      
    def distinctNames(self, ideas : List[str]) -> int:        
        h = defaultdict(set)
        for w in ideas:
            h[w[0]].add(w[1:])
        r = 0
        for c1 in h:
            for c2 in h:
                if c1 != c2:
                    c = sum([1 for w in h[c1] if w in h[c2]])
                    r += ((len(h[c1]) - c) * (len(h[c2]) - c))
        return r