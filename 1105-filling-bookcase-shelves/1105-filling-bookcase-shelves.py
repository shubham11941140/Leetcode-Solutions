class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        pw = [0] * (n + 1)
        for i in range(1, n + 1):
            pw[i] = pw[i - 1] + books[i - 1][0]        
        dp = [0] + [float("inf")] * n
        for i in range(1, n + 1):
            for j in reversed(range(i)): # j is the last book in previous row
                if (pw[i] - pw[j] <= shelfWidth):
                    dp[i] = min(dp[i], dp[j] + max([h for _, h in books[j: i]]))
                else:
                    break        
        return dp[-1]       