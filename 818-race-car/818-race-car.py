from collections import defaultdict, deque


class Solution:

    @lru_cache
    def racecar(self, target: int) -> int:
        q = []
        q.append((0, 1, 0))
        v = defaultdict(lambda: defaultdict(lambda: False))
        # v = set()
        v[0][1] = True
        # v.add((0, 1))
        while q:
            p, s, steps = q.pop(0)
            if p == target:
                return steps
            npa = p + s
            nsa = s * 2
            if not v[npa][nsa]:
                q.append((npa, nsa, steps + 1))
                v[npa][nsa] = True
            if (s > 0 and p + s > target) or (s < 0 and p + s < target):
                npr = p
                nsr = -1 if s >= 0 else 1
                if not v[npr][nsr]:
                    q.append((npr, nsr, steps + 1))
                    v[npr][nsr] = True
