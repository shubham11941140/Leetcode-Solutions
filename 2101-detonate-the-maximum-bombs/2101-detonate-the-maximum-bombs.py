class Solution:

    def dfs(self, curr, d):
        d.add(curr)
        for i in self.u:
            if i not in d:
                if sqrt((curr[0] - i[0])**2 + (curr[1] - i[1])**2) <= curr[2]:
                    self.dfs(i, d)

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        nb = [(i[0], i[1], i[2]) for i in bombs]
        self.u = nb.copy()
        c = Counter(nb)
        m = []
        for i in nb:
            d = set()
            self.dfs(i, d)
            m.append(sum([c[i] for i in d]))
        return max(m)
