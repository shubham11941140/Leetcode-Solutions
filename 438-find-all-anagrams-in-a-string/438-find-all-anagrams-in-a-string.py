class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        k = len(p)
        p = sorted(list(p))
        if n < 100 and k < 100:
            return [i for i in range(n) if sorted(s[i:i + k]) == p]
        ans = []
        print(n, k)
        
        i = 0
        while i < n - k + 1:            
            if sorted(s[i:i + k]) == p:
                ans.append(i)
                while i < n - k and s[i] == s[i + k]:                      
                    ans.append(i)
                    i += 1
                    
            i += 1
        i = n - k
        if sorted(s[n - k:n]) == p:
            ans.append(n - k)
        #print(ans[-1])
        return set(ans)