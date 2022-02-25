class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        a = list(s)
        while '-' in a:
            a.remove('-')
        print(a)
        a = a[::-1]
        ans = ""
        for i in range(len(a)):
            ans += a[i]
            if (i + 1) % k == 0 and i != len(a) - 1:
                ans += "-"
        print(ans)
        return ''.join(ans[::-1])
        
            
        