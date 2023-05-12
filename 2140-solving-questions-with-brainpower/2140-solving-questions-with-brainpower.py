class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0
            return max(dfs(i+1),questions[i][0] + dfs(i+questions[i][1]+1))
        return dfs(0)