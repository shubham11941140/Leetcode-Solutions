class Solution:

    def dfs(self, g, node, visited, cc):
        for i in g[node]:
            if i not in visited:
                visited.add(i)
                cc.append(i)
                self.dfs(g, i, visited, cc)

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        A = s1
        B = s2
        S = baseStr
        # Make a graph
        graph = {chr(i): chr(i) for i in range(97, 123)}
        g = collections.defaultdict(list)
        # Add edges based on equivalence
        n = len(A)
        for i in range(n):
            if A[i] != B[i]:
                g[A[i]].append(B[i])
                g[B[i]].append(A[i])
        print(g)
        # Find all connected components in the graph
        visited = set()
        acc = []
        for i in g:
            if i not in visited:
                visited.add(i)
                cc = [i]
                self.dfs(g, i, visited, cc)
                acc.append(cc)
        print(acc)
        sacc = [sorted(i) for i in acc]
        for j in S:
            for i in sacc:
                if j in i:
                    S = S.replace(j, i[0])
        return S
