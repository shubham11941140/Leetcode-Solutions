class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s, 0, [], res)
        return res
    
    def dfs(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append('.'.join(path))
            return
        for i in range(1, 4):
            if i <= len(s):
                if i == 1:
                    self.dfs(s[i:], index + 1, path + [s[:i]], res)
                elif i == 2 and s[0] != '0':
                    self.dfs(s[i:], index + 1, path + [s[:i]], res)
                elif i == 3 and s[0] != '0' and int(s[:3]) <= 255:
                    self.dfs(s[i:], index + 1, path + [s[:i]], res)        