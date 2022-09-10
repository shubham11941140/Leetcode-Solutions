class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        b = []        
        for c in range(1001):
            ans = 0
            for cit in citations:
                if cit >= c:
                    ans += 1
            if ans >= c:
                b.append(c)
        return b[-1]
                
        