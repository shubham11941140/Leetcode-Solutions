class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        res = []
        for word in words:
            if self.dfs(word, words):
                res.append(word)
        return res

    def dfs(self, word, words):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in words and suffix in words:
                return True
            if prefix in words and self.dfs(suffix, words):
                return True
        return False        