import string


class Solution:

    def equationsPossible(self, equations: List[str]) -> bool:
        d = {}
        for i in string.ascii_lowercase:
            d[i] = [i]
        for i in equations:
            if i[1] == "=":
                d[i[0]].append(i[3])
                d[i[3]].append(i[0])
        for i in equations:
            if i[1] == "!":
                q = [i[0]]
                visited = set()
                while q:
                    curr = q.pop(0)
                    visited.add(curr)
                    if curr == i[3]:
                        return False
                    q += [j for j in d[curr] if j not in visited]
        return True
