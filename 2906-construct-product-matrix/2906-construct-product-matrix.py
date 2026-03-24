class Solution:
    def constructProductMatrix(self, g: List[List[int]]) -> List[List[int]]:
        f = lambda a:[1, *accumulate(a, lambda q, v : q * v % 12345)]
        pref,suff = f(chain(*g)), f(chain(*map(reversed,reversed(g))))[::-1]
        b = (v * u % 12345 for v,u in zip(pref, suff[1:]))
        return [*zip(*[iter(b)] * len(g[0]))]        