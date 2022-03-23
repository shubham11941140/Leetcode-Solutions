from math import ceil

class Solution:
    
    def iterate(self, s, t, ans):
        rep = set()
        rep.add(t)
        for steps in range(40000):
            for i in ans[steps]:
                if i == s:
                    return steps
            for i in ans[steps]:
                if i + 1 not in rep:
                    ans[steps + 1].append(i + 1)
                    rep.add(i + 1)                
                if i % 2 == 0 and i // 2 not in rep:
                    ans[steps + 1].append(i // 2)  
                    rep.add(i // 2)
    
    def brokenCalc(self, startValue: int, target: int) -> int:
        if target < startValue:
            return startValue - target    
                
        ans = [[] for i in range(50000)]
        ans[0].append(target)
        steps = self.iterate(startValue, target, ans)
        #print(steps)
        #print(ans)
        if steps == None:
            p = ceil(target / 2)
            if target % 2:
                p -= 1
            return startValue + 1 - p
        return steps