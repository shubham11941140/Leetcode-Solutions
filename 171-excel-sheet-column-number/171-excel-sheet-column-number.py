class Solution:
    
    def findsum(self, n):
        p = 0
        for i in range(1, n + 1):
            p += (26 ** i)
        return p
    
    def titleToNumber(self, columnTitle: str) -> int:        
        s = columnTitle
        l = list(s)
        n = len(l)
        
        
        # wORk byfixing the length
        # 1st letter
        # EZZZZ
        # FAMAJ
        
        # TODO BEFORE
        o = self.findsum(n - 1)
        print(o)
        # At place acheived
        fix = 0
        for i in range(n):
            val = ord(s[i]) - ord('A')
            rem = n - i - 1
            p = pow(26, rem)
            delta = val * p
            print("D", val, rem, delta)
            fix += delta
        print("F", fix)
        return o + fix + 1
        
        p = 0
        
        for i in range(n):
            val = ord(s[i]) - ord('A') + 1
            k = val * self.findsum(n - i)
            print(k)
            p += k
        return p
        
        
        for i in range(1, n):
            p += (26 ** i)
        print(p)
        # All of nth size
        ans = 1
        for i in l:
            print(i)
            val = ord(i) - ord('A')
            ans *= (val + 1)
        print(ans)
        return p + ans + ord(i[-1]) - ord('A')