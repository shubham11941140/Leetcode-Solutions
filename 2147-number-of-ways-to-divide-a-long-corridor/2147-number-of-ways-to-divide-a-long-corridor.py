class Solution:
    def numberOfWays(self, c: str) -> int:
        return prod(len(m.group(1)) + 1 for m in re.finditer(r'S(P*)S', c[c.find('S') + 1:])) % (10 ** 9 + 7) if (s := c.count('S')) and s % 2 == 0 else 0