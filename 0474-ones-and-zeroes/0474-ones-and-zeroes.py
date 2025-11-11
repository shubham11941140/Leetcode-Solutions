class Solution:
    
    @cache
    def rec(self, i, j, idx):
        if i < 0 or j < 0:
            return -10
        if idx == len(self.a):
            return 0
        return max(self.rec(i, j, idx + 1), 1 + self.rec(i - self.a[idx][0], j - self.a[idx][1], idx + 1))
    
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.a = [[s.count('0'), s.count('1')] for s in strs]
        return self.rec(m, n, 0)
                        