class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        # Solve using connected componenets of a graph
        d = {}
        k = 0
        for i in equations:
            for j in i:
                if j not in d:
                    d[j] = k
                    k += 1
        adj = [[] for i in range(k)]
        for i in range(len(values)):
            a, b = equations[i]
            adj[d[a]].append([d[b], values[i]])
            adj[d[b]].append([d[a], 1 / values[i]])
        ans = []
        for a, b in queries:
            if a not in d or b not in d:
                ans.append(-1)
                continue
            elif a == b:
                ans.append(1)
                continue
            else:
                q = []
                path = []
                src = d[a]
                dst = d[b]
                path.append(src)
                q.append(path.copy())
                flag = False
                while q:
                    path = q.pop(0)
                    last = path[-1]
                    if last == dst:
                        flag = True
                        break
                    for i, j in adj[last]:
                        if i not in path:
                            q.append(path.copy() + [i])
                if not flag:
                    ans.append(-1)
                    continue
                f = 1
                for i in range(len(path) - 1):
                    for v, w in adj[path[i]]:
                        if v == path[i + 1]:
                            f *= w
                ans.append(f)
        return ans
