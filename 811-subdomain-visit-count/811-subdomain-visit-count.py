class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        d = {}
        for i in cpdomains:
            c, s = i.split()
            print(c)
            c = int(c)
            p = s.split('.')
            print(p)
            if len(p) == 3:
                s1 = s
                s2 = '.'.join(p[1:])
                s3 = p[-1]
                for k in [s1, s2, s3]:
                    d[k] = int(d[k] + c if k in d else c)
                print(s1,s2,s3)
            elif len(p) == 2:
                s1 = s
                s2 = p[-1]
                for k in [s1, s2]:
                    d[k] = int(d[k] + c if k in d else c)                
        print(d)
        ans = []
        for i in d:
            h = str(d[i]) + " " + i
            ans.append(h)
        return ans
        
        
        