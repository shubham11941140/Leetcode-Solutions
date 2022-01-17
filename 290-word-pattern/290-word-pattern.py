class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a = s.split()
        p = list(pattern)
        b = []
        for i in a:
            if i not in b:
                b.append(i)
        print(b)
        d = []
        for i in p:
            if i not in d:
                d.append(i)
        print(b)
        c = [b.index(i) for i in a]
        print(c)
        print(d)
        e = [d.index(i) for i in p]
        print(e)
        return c == e
        