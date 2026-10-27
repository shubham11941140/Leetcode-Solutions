class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = []
        for i in range(m):
            if i == 0:
                val = "." * n
                ans.append(val)
            else:
                val = "#" * (n - 1) + "."
                ans.append(val)
        return ans
        