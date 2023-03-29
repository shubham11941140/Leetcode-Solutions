class Solution:
    def comp(self, a, i, n):
        val = 0
        for j in range(i, n):
            val += a[j] * (j - i + 1)
        return val

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        r = 0
        for i in range(n):
            ans = self.comp(satisfaction, i, n)
            r = max(r, ans)
        return r
