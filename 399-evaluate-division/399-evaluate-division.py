class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Solve using connected componenets of a graph
        d = {}
        k = 0
        for i in equations:
            for j in i:
                if j not in d:
                    d[j] = k
                    k += 1
        print(d, k)
        # Graph
        adj = [[] for i in range(k)]
        for i in range(len(values)):
            a, b = equations[i]
            u, v = d[a], d[b]
            w1 = values[i]
            w2 = 1/w1
            adj[u].append([v, w1])
            adj[v].append([u, w2])
        print(adj)
        # Graph is done
        # Deal with queries
        ans = []
        for a, b in queries:
            if a not in d or b not in d:
                ans.append(-1)
                continue
            elif a == b:
                ans.append(1)
                continue
            else:
                # Check if they lie in the same component of the graph
                # If they dont lie return -1
                # ELse return path product
                # Create a queue which stores
                # the paths
                print("BEFORE BFS")
                q = []

                # Path vector to store the current path
                path = []
                src = d[a]
                dst = d[b]
                path.append(src)
                q.append(path.copy())
                flag = False

                while q:
                    path = q.pop(0)
                    last = path[len(path) - 1]

                    # If last vertex is the desired destination
                    # then print the path
                    if (last == dst):
                        #print("PATH", path)
                        print("REACHED DEST")
                        flag = True
                        break

                    # Traverse to all the nodes connected to
                    # current vertex and push new path to queue
                    for i, j in adj[last]:
                        if i not in path:
                            newpath = path.copy()
                            newpath.append(i)
                            q.append(newpath)
                print("P", path)
                if not flag:
                    ans.append(-1)
                    continue
                f = 1
                for i in range(len(path) - 1):
                    p = path[i]
                    q = path[i + 1]
                    for v, w in adj[p]:
                        if v == q:
                            print("WEI", w)
                            f *= w
            ans.append(f)
            print("ANS", ans)
        print("76", ans)
        return ans

            