class Solution:
    
    def match(self, s, t):
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
    
    @cache
    def check(self, str1, str2):
        m = len(str1)
        n = len(str2)

        j = 0    # Index of str1
        i = 0    # Index of str2

        # Traverse both str1 and str2
        # Compare current character of str2 with
        # first unmatched character of str1
        # If matched, then move ahead in str1

        while j < m and i < n:
            if str1[j] == str2[i]:
                j = j+1
            i = i + 1

        # If all characters of str1 matched,
        # then j is equal to m
        return j == m        
        
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        return len([i for i in words if self.check(i, s)])
        