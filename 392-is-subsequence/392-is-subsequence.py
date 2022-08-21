class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # solve using DP
        # Simple ARR traversal
        ns = len(s)
        nt = len(t)
        i = 0
        j = 0
        while i < ns:
            while j < nt:
                if i < ns and s[i] == t[j]:
                    i += 1
                j += 1
            if j == nt and i != ns:
                return False
        return True
                    
        
