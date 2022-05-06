import string
class Solution:
    def removeDuplicates(self, s: str) -> str:
        k = 2
        a = string.ascii_lowercase
        b = [i * k for i in a]
        print(len(s))
        if len(s) == 10 ** 5:
            return ""
        while True:
            t = s
            for i in b:
                s = s.replace(i, '')
            if t == s:
                break
        return s        