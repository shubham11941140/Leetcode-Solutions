class Solution:

    def dist(self, cod1, cod2):
        return math.sqrt(
            math.pow(cod1[0] - cod2[0], 2) + math.pow(cod1[1] - cod2[1], 2))

    def dfs(self, curr, d, u):
        d.add(curr)
        # print(d, u)
        for i in u:
            if i not in d:
                # print(curr, i)
                if self.dist(curr, i) <= curr[2]:
                    self.dfs(i, d, u)

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        nb = [(i[0], i[1], i[2]) for i in bombs]
        c = Counter(nb)
        # print(nb)
        m = []
        for i in nb:
            d = set()
            u = nb.copy()
            self.dfs(i, d, u)
            s = len(d)
            # print(s)
            for i in d:
                b = c[i]
                if b > 1:
                    s += b - 1
            m.append(s)
        return max(m)
