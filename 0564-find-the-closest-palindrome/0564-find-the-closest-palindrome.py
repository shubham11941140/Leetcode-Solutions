class Solution:

    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        c = set()
        if n == "1":
            return "0"
        p = int(n[: (l + 1) // 2])
        for i in [-1, 0, 1]:
            new_prefix = str(p + i)
            c.add(new_prefix + (new_prefix[:-1][::-1] if l % 2 else new_prefix[::-1]))
        c.add(str(10 ** (l - 1) - 1))
        c.add(str(10**l + 1))
        c.discard(n)
        return min(c, key=lambda x: (abs(int(x) - int(n)), int(x)))
