class Solution:
    def c(self, idx, s):
        if idx == self.l:
            return len(s)
        res = 0
        if len(set(s + self.res[idx])) == len(s + self.res[idx]):
            res = max(res, self.c(idx + 1, s + self.res[idx]))
        res = max(res, self.c(idx + 1, s))
        return res    
    def maxLength(self, arr: List[str]) -> int:
        self.res = [i for i in arr if len(set(i)) == len(i)]
        self.l = len(self.res)
        return self.c(0, '')  