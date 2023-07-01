class Solution:

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        self.ans = math.inf

        def dfs(idx):
            if idx == n:
                self.ans = min(self.ans, max(children))
                return

            seen = set()
            for i in range(k):
                if children[i] in seen:
                    continue
                seen.add(children[i])
                children[i] += cookies[idx]
                if children[i] < self.ans:
                    dfs(idx + 1)
                children[i] -= cookies[idx]

        children = [0 for i in range(k)]
        dfs(0)
        return self.ans
