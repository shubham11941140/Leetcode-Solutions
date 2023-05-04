class Solution:

    def predictPartyVictory(self, senate: str) -> str:
        l = len(senate)
        d = collections.deque()
        r = collections.deque()
        for i, c in enumerate(senate):
            if c == "R":
                r.append(i)
            else:
                d.append(i)
        while r and d:
            p = r.popleft()
            q = d.popleft()
            if p < q:
                r.append(p + l)
            else:
                d.append(q + l)
        if r:
            return "Radiant"
        else:
            return "Dire"
