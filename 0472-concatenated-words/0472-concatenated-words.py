class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.w = set(words)
        return [i for i in words if self.dfs(i)]

    def dfs(self, word):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in self.w:
                if suffix in self.w or self.dfs(suffix):
                    return True
        return False