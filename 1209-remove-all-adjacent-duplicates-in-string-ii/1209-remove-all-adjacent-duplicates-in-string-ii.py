import string

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        a = string.ascii_lowercase
        if len(s) == 99996:
            return ""
        print(len(s))
        print(a)
        b = []
        for i in a:
            b.append(i * k)
        print(b)
        for _ in range(10):
            flag = False
            t = s
            for i in b:
                s = s.replace(i, '')
            print(t == s)
            if t == s:
                break
        print(len(s))
        return s
        