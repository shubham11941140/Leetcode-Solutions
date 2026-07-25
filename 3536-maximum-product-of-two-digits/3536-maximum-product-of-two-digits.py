class Solution:
    def maxProduct(self, n: int) -> int:
        a = [int(i) for i in str(n)]
        l = len(a)
        return max([a[i] * a[j] for i in range(l) for j in range(i + 1, l)])