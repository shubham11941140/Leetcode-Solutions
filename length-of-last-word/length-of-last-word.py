class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = ' ' + s
        l = list(s)[::-1]
        if ' ' not in l:
            return len(l)
        t = 0
        while l[t] == ' ':
            t += 1
        i = t
        while l[i] != ' ':
            i += 1
        return i - t
        
        
        