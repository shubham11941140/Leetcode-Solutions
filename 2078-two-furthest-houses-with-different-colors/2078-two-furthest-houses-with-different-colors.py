class Solution:
    def maxDistance(self, colors: List[int]) -> int:        
        n = len(colors)
        for i in range(n):
            if colors[i] != colors[~0] or colors[~i] != colors[0]:
                return n - (i + 1)            