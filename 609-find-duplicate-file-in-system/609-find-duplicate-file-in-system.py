class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        s = dict()
        for i in paths:
            d = i.split()
            for j in d[1:]:
                f, c = j.split('(')
                s[c] = s[c] + [d[0] + '/' + f] if c in s else [d[0] + '/' + f]
        return [i for i in s.values() if len(i) > 1]
        