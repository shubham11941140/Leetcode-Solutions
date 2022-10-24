class Solution:

    def getFolderNames(self, names: List[str]) -> List[str]:
        res = []
        d = {}
        for i in names:
            if i not in d:
                d[i] = 1
                res.append(i)
            else:
                while i + "(" + str(d[i]) + ")" in d:
                    d[i] += 1
                res.append(i + "(" + str(d[i]) + ")")
                d[i + "(" + str(d[i]) + ")"] = 1
                d[i] += 1
        return res
