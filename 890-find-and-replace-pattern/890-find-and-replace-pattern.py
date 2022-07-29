class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        n = len(pattern)
        ans = []
        for w in words:
            d = dict()
            flag = True
            for i in range(n):
                s = pattern[i]
                if s not in d:
                    d[s] = w[i]
                else:
                    # d[s] exist
                    if d[s] != w[i]:
                        flag = False
                        break
            if flag:
                print(d)
                print(len(d))
                if len(set(d.values())) == len(d):
                    ans.append(w)
        return ans
                    
                
                