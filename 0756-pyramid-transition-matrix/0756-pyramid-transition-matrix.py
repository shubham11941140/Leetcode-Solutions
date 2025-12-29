class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        d = defaultdict(list)
        for t in allowed: d[*t[:2]].append(t[2])
        return (f:=cache(lambda s:len(s)==1 or 
            any(map(f,product(*(d[p] for p in pairwise(s)))))))(bottom)        