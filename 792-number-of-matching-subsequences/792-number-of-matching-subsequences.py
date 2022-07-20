class Solution:
    
    @cache
    def check(self, s):
        m = len(s)
        j = 0
        i = 0
        while j < m and i < self.n:
            if s[j] == self.s[i]:
                j += 1
            i += 1
        return j == m        
        
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        self.s = s
        self.n = len(s)
        return len([1 for i in words if self.check(i)])
        