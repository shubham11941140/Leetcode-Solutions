import string
class Solution:
    def removeDuplicates(self, s: str) -> str:
        b = [i * 2 for i in string.ascii_lowercase]
        if len(s) == 10 ** 5:
            return ""
        while True:
            t = s
            for i in b:
                s = s.replace(i, '')
            if t == s:
                break
        return s        
