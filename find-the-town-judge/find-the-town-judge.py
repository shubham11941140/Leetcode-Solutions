class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        flag = False
        for i in trust:
            u = i[0] - 1
            v = i[1] - 1
            #adj[u].append(v)
            adj[v].append(u)
        for i in range(n):
            t = adj[i]
            if len(t) == n - 1:
                c = 0
                for j in range(n):
                    if i != j:
                        if i not in adj[j]:
                            c += 1
                if c == n - 1:
                    flag = True
                    ans = i + 1
        return ans if flag else -1
                    
            
        