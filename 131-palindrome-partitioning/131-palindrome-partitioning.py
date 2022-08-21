class Solution:

    def generate(self, s, idx, ans, final):
        if idx == len(s):
            final.append(ans.copy())
        else:
            for i in range(idx, len(s)):
                val = s[idx:i + 1]
                ans.append(val)
                self.generate(s, i + 1, ans, final)
                ans.pop()

    @staticmethod
    def ispallindrome(a):
        return a == a[::-1]

    def check_pallindrome(self, final):
        return [
            i for i in final
            if len([1 for j in i if self.ispallindrome(j)]) == len(i)
        ]

    def partition(self, s: str) -> List[List[str]]:
        final = []
        self.generate(s, 0, [], final)
        return self.check_pallindrome(final)
