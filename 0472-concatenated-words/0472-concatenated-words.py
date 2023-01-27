class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.w = set(words)
        return [i for i in words if self.dfs(i)]

    def dfs(self, word):
        for i in range(1, len(word)):
            p = word[:i]
            s = word[i:]
            if p in self.w and (s in self.w or self.dfs(s)):
                return True
        return False