class Solution:    
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        return len([1 for i in range(n) for j in range(i + 1, n + 1) if s[i:j] == s[i:j][::-1]])

        
