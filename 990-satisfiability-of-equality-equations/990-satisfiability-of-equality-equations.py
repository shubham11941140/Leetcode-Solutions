import string
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        d = {}
        for i in string.ascii_lowercase:
            d[i] = [i]

        # Construct a complete graph
        for i in equations:
            if i[1:3] == '==':
                d[i[0]].append(i[3])
                d[i[3]].append(i[0])
        print(d)
        for i in equations:
            if i[1:3] == '!=':
                a, b = i[0], i[3]
                q = [a]
                visited = set()
                while q:
                    curr = q.pop(0)
                    visited.add(curr)
                    if curr == b:
                        return False
                    for i in d[curr]:
                        if i not in visited:
                            q.append(i)
        return True

  