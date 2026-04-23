class Solution:

    def dfs(self, strs, i, visited):
        visited.add(i)
        for j in range(len(strs)):
            if self.isSimilar(strs[i], strs[j]) and j not in visited:
                self.dfs(strs, j, visited)

    # calculate the similarity of two strings
    def isSimilar(self, str1, str2):
        return sum([1 for i in range(len(str1)) if str1[i] != str2[i]]) <= 2

    def numSimilarGroups(self, strs: List[str]) -> int:
        visited = set()
        group = 0
        for i in range(len(strs)):
            if i not in visited:
                group += 1
                self.dfs(strs, i, visited)
        return group
