from collections import Counter
from string import ascii_lowercase
class Solution:
    
    def lcs(self, X, Y):
        # find the length of the strings
        m = len(X)
        n = len(Y)

        # declaring the array for storing the dp values
        L = [[None]*(n + 1) for i in range(m + 1)]

        """Following steps build L[m + 1][n + 1] in bottom up fashion
        Note: L[i][j] contains length of LCS of X[0..i-1]
        and Y[0..j-1]"""
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0 :
                    L[i][j] = 0
                elif X[i-1] == Y[j-1]:
                    L[i][j] = L[i-1][j-1]+1
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])

        # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
        return L[m][n]    
    
    
    def minDistance(self, word1: str, word2: str) -> int:
        
        l = self.lcs(word1, word2)
        return (len(word1) + len(word2)) - (2 * l)
        
        
        
        c1 = Counter(word1)
        c2 = Counter(word2)
        print(c1, c2)
        print(ascii_lowercase)
        ans = 0
        for i in ascii_lowercase:
            if i in c1 and i in c2:
                ans += abs(c1[i] - c2[i])
            elif i in c1 and i not in c2:
                ans += c1[i]
            elif i in c2 and i not in c1:
                ans += c2[i]
        return ans
                
        
        