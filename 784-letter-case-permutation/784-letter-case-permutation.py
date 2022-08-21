class Solution:
    
    def rec(self, s, idx, a, ans):
        if idx == len(s):
            ans.append(a)
            return
        if s[idx].isalpha():
            self.rec(s, idx + 1, a + s[idx].upper(), ans)
            self.rec(s, idx + 1, a + s[idx].lower(), ans)
        else:
            self.rec(s, idx + 1, a + s[idx], ans)
            
    def letterCasePermutation(self, s: str) -> List[str]:        
        idx = 0
        a = ''
        ans = []
        self.rec(s, idx, a, ans)
        return ans
