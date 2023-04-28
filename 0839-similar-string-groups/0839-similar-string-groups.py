class Solution:
    
    def dfs(self, strs, i, visited):
        #add current string to memo
        visited.add(i)
        for j in range(len(strs)):
            if self.isSimilar(strs[i], strs[j]) and j not in visited:
                self.dfs(strs, j ,visited)
                
    # calculate the similarity of two strings            
    def isSimilar(self, str1, str2):
        diff_count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff_count += 1
        return diff_count <= 2                
    def numSimilarGroups(self, strs: List[str]) -> int:
        visited = set()
        group = 0
        for i in range(len(strs)):
            if i not in visited:
                group += 1
                self.dfs(strs, i ,visited)
        
        return group        