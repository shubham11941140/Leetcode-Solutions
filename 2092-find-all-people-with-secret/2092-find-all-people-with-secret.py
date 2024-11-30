class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        q = [(0, 0), (0, firstPerson)]

        g = collections.defaultdict(list)
        for p, p1, t in meetings:
            g[p].append((p1, t))
            g[p1].append((p, t))

        a = set()
        while q:
            t, p = heappop(q)
            if p in a:
                continue
            a.add(p)
            for pii, m in g[p]:
                if m >= t:
                    heappush(q, (m, pii))
        return list(a)
