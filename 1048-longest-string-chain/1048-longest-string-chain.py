class Solution:

    @staticmethod
    def can(word1, word2):
        if len(word1) + 1 == len(word2):
            for i in range(len(word2)):
                w = list(word2)
                w.pop(i)
                if word1 == "".join(w):
                    return True
        return False

    def dfs(self, node, dp, vis):
        vis[node] = True
        for i in range(0, len(self.adj[node])):
            if not vis[self.adj[node][i]]:
                self.dfs(self.adj[node][i], dp, vis)
            dp[node] = max(dp[node], 1 + dp[self.adj[node][i]])

    def long(self):
        dp = [0] * (self.v + 1)
        vis = [False] * (self.v + 1)
        for i in range(self.v + 1):
            if not vis[i]:
                self.dfs(i, dp, vis)

        ans = 0

        # Traverse and find the maximum of all dp[i]
        for i in range(self.v + 1):
            ans = max(ans, dp[i])

        return ans

    def longestStrChain(self, words: List[str]) -> int:
        # Make a graph of which can act as predessor
        # BFS from every node based on distance
        # Find max distance
        # Return
        # Make a graph
        # if words in [["a","aa","aab","aabb","bbaac"], ["a","ab","ac","bd","abc","abd","abdd"]]:
        # return 4
        self.v = len(words)
        self.adj = [[] for i in range(self.v + 1)]
        for i in range(self.v):
            for j in range(self.v):
                if self.can(words[i], words[j]):
                    self.adj[i].append(j)
        print(self.adj)
        # DAG is done
        # Longest chain I need to find connecting
        ans = self.long()
        print(ans)
        return ans + 1
