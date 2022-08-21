class Solution:

    def freq(self, a):
        d = {}
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return d

    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        f = self.freq(words)
        words.sort()
        lwords = [len(i) for i in words]
        tlen = sum(lwords)
        lb = min(lwords)
        ub = max(lwords)
        ans = []
        for i in range(len(s)):
            b = s[i:i+tlen]
            idx = 0
            check = []
            while idx <= tlen:  
                Flag = False
                #print(idx)
                for j in range(lb, ub + 1):
                    c = b[idx:idx + j]
                    if c in words:
                        check.append(c)
                        idx += j
                        Flag = True
                        break
                if not Flag:
                    break
            if sorted(check) == words and self.freq(check) == f:
                ans.append(i)
        return ans




