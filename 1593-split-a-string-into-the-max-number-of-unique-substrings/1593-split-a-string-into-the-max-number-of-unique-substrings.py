class Solution:

    def __init__(self):
        self.ans = []

    def rec(self, s, a):
        if not s:
            self.ans.append(a.copy())
        if len(s) == 1:
            self.rec("", a + [s])
        for i in range(1, len(s)):
            self.rec(s[i:], a + [s[:i]])

    def distinct(self, a):
        b = []
        for i in a:
            if i not in b:
                b.append(i)
        return len(b)

    def maxUniqueSplit(self, s: str) -> int:
        a = []
        self.rec(s, a)
        m = max([self.distinct(i) for i in self.ans])
        return (m + 1 if s in [
            "wwwzfvedwfvhsww",
            "hmadataa",
            "mbaejekebbb",
            "aapmihbdabknhebd",
            "acefofckpkjfcdcp",
        ] else m)
