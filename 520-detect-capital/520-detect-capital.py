class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        a = [word[i].isupper() for i in range(n)]
        if len(set(a)) == 1 or a == [True] + [False] * (n - 1):
            return True
        return False
        
