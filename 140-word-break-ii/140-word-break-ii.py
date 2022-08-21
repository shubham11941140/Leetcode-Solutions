class Solution:
    
    def space(self, s, idx, a):
        if idx == len(s):
            a.append(s)
            return
        self.space(s, idx + 1, a)
        self.space(s[:idx] + " " + s[idx:], idx + 2, a)
            
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        a = []
        self.space(s, 0, a)
        ans = []
        for i in a:
            k = i.split(' ')
            if len(k) == len([1 for j in k if j in wordDict]):
                ans.append(i)
        return ans
                    
        
        
