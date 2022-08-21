class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = list(s)
        n = len(s)
        l = 0
        for i in range(n):
            k1 = 0
            while i + k1 < n and i >= k1 and s[i + k1] == s[i - k1]:
                k1 += 1
            k2 = 0
            while i + k2 + 1 < n and i - k2 >= 0 and s[i - k2] == s[i + 1 + k2]:
                k2 += 1      
            if 2 * k1 - 1 >= l:
                l = 2 * k1 - 1
                ans = t[i - k1 + 1:i + k1] 
            if 2 * k2 >= l:
                l = 2 * k2
                ans = t[i - k2 + 1:i + k2 + 1] 
        return ''.join(ans)


