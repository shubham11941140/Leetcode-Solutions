class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()  
        for c in reversed(range(1001)):
            ans = 0
            for cit in reversed(citations):
                if cit < c:
                    break
                ans += 1
            if ans >= c:
                return c                
        