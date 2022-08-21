class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = list(t)
        for i in s:
            t.remove(i)
        return ''.join(t)
        
