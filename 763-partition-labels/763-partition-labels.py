class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        ans = []
        for i in range(1, n):
            a = s[:i]
            b = s[i:]
            c = True
            for k in a:
                if k in b:
                    c = False
                    break
            if c:
                ans.append(i)
                print(i)
        print(n)
        ans.append(n)
        print(ans)
        r = [ans[0]]
        for i in range(1, len(ans)):
            r.append(ans[i] - ans[i - 1])
        return r
        
                    
            
        