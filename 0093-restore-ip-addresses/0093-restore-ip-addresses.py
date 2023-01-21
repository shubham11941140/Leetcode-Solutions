class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.r = []
        self.dfs(s, 0, [])
        return self.r

    def dfs(self, s, index, path):
        if index == 4:
            if not s:
                self.r.append(".".join(path))
            return
        for i in range(1, 4):
            if i <= len(s):
                if i == 1:
                    self.dfs(s[i:], index + 1, path + [s[:i]])
                elif i == 2 and s[0] != "0":
                    self.dfs(s[i:], index + 1, path + [s[:i]])
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], index + 1, path + [s[:i]])
