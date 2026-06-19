class Solution:

    def dfs(self, g, node, v, cc):
        for i in g[node]:
            if i not in v:
                v.add(i)
                cc.append(i)
                self.dfs(g, i, v, cc)

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        g = collections.defaultdict(list)
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                g[s1[i]].append(s2[i])
                g[s2[i]].append(s1[i])
        v = set()
        a = []
        for i in g:
            if i not in v:
                v.add(i)
                cc = [i]
                self.dfs(g, i, v, cc)
                a.append(cc)
        sa = [sorted(i) for i in a]
        for j in baseStr:
            for i in sa:
                if j in i:
                    baseStr = baseStr.replace(j, i[0])
        return baseStr
