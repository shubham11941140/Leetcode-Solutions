class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        t = []
        for i in matches:
            t += i
        t = set(t)
        w = Counter([x for [x, y] in matches])
        l = Counter([y for [x, y] in matches])
        print(w, l)
        s = []
        for i in l:
            if l[i] == 1:
                s.append(i)
        f = []
        for i in t:
            if i not in l:
                f.append(i)
        print(f, s)
        return [sorted(f), sorted(s)]
