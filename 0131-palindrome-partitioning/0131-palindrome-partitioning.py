class Solution:

    def generate(self, s, idx, ans):
        if idx == len(s):
            self.final.append(ans.copy())
        else:
            for i in range(idx, len(s)):
                val = s[idx:i + 1]
                ans.append(val)
                self.generate(s, i + 1, ans)
                ans.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.final = []
        self.generate(s, 0, [])
        return [
            i for i in self.final
            if len([1 for j in i if j == j[::-1]]) == len(i)
        ]
