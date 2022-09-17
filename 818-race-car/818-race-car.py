from collections import defaultdict, deque
class Solution:                          
    @lru_cache
    def racecar(self, target: int) -> int:
        q = deque()
        q.append((0, 1, 0))
        v = defaultdict(lambda: defaultdict(lambda: False))
        v[0][1] = True
        while q:
            p, s, steps = q.popleft()
            if p == target:
                return steps
            if not v[p + s][s * 2]:
                q.append((p + s, s * 2, steps + 1))  
                v[p + s][s * 2] = True
            if (s > 0 and p + s > target) or (s < 0 and p + s < target) and not v[p][(-1 if s >= 0 else 1)]:
                q.append((p, (-1 if s >= 0 else 1), steps + 1))
                v[p][(-1 if s >= 0 else 1)] = True