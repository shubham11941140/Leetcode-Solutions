class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.t = defaultdict(list)        
        for i in range(1, len(parent)):
            self.t[parent[i]].append(i)
        self.ans = 1
        self.s = s
        self.dfs(0)
        return self.ans

    def dfs(self, i):
        if i not in self.t:
            return 1
        r = 1
        for j in self.t[i]:
            l = self.dfs(j)
            if self.s[i] != self.s[j]:
                self.ans = max(self.ans, l + r)
                r = max(r, l + 1)
        return r
        