class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # Path (content)
        s = dict()
        for i in paths:
            d = i.split()
            #print(d)
            di = d[0]
            for j in d[1:]:
                f, c = j.split('(')
                print(c, di + '/' + f)
                fp = di + '/' + f
                if c in s:
                    s[c].append(fp)
                else:
                    s[c] = [fp]
        print(s)
        return [i for i in s.values() if len(i) > 1]
        #return s.values()
        