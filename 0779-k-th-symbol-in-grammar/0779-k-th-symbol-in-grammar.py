class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if k <= 2 ** (n - 2):
            return self.kthGrammar(n - 1, k)
        return 1 - self.kthGrammar(n - 1, k - 2 ** (n - 2))
