class Solution:

    def diff(self, word1, word2):
        return False if len(word1) != len(word2) else len([1 for c1, c2 in zip(word1, word2) if c1 != c2]) == 1

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        dp = [1] * n
        parent = [-1] * n
        maxi = 0
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and self.diff(words[i], words[j]) and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            maxi = max(maxi, dp[i])
        result = []
        for i in range(n):
            if dp[i] == maxi:
                while i != -1:
                    result.append(words[i])
                    i = parent[i]
                break
        return result[::-1]        