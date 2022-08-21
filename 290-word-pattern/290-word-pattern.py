class Solution:

    @staticmethod
    def wordPattern(pattern: str, s: str) -> bool:
        a = s.split()
        p = list(pattern)
        b = []
        for i in a:
            if i not in b:
                b.append(i)
        d = []
        for i in p:
            if i not in d:
                d.append(i)
        return [b.index(i) for i in a] == [d.index(i) for i in p]
