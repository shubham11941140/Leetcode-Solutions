class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        flag = False
        for i in trust:
            adj[i[1] - 1].append(i[0] - 1)
        for i in range(n): 
            if len(adj[i]) == n - 1 and len([j for j in range(n) if i != j and i not in adj[j]]) == n - 1:
                    flag = True
                    ans = i + 1
        return ans if flag else -1



