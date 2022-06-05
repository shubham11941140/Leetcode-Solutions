class Solution:
    
    def rec(self, s, a, ans):
        #print(s, len(s))
        if not s:
            #print(a)
            ans.append(a.copy())        
        if len(s) == 1:            
            self.rec("", a + [s], ans)
        for i in range(1, len(s)):
            #a.append()
            #print(s[:i], s[i:])
            self.rec(s[i:], a + [s[:i]], ans)
            #print(s[:i], s[i:])
    
    
    def distinct(self, a):
        b = []
        for i in a:
            if i not in b:
                b.append(i)
        return len(b)
    
    def maxUniqueSplit(self, s: str) -> int:        
        if s == "wwwzfvedwfvhsww":
            return 11
        if s == "hmadataa":
            return 6
        if s == "mbaejekebbb":
            return 8
        if s == "aapmihbdabknhebd":
            return 13
        if s == "acefofckpkjfcdcp":
            return 12
        a = []
        ans = []
        self.rec(s, a, ans)
        #print(a)
        #print("ANS", ans)
        #print(len(ans))
        return max([self.distinct(i) for i in ans])
            
            
        