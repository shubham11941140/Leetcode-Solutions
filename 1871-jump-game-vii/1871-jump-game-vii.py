class Solution:
    def canReach(self, s: str, m: int, M: int) -> bool:
        q, k, n = [0], 1, len(s)
        for i in q:
            q += [j for j in range(max(i + m, k), min(i + M + 1, n)) if s[j] == '0']
            k = i + M + 1
        return q[-1] == n - 1        