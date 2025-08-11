class Solution:

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n - 1)
        res = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            res.append(str(j - i))
            res.append(s[i])
            i = j
        return "".join(res)
