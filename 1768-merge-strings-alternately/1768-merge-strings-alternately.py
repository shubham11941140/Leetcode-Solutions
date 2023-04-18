class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = min(len(word1), len(word2))
        result = [(word1[i] + word2[i]) for i in range(m)]
        return ''.join(result) + word1[m:] + word2[m:]        