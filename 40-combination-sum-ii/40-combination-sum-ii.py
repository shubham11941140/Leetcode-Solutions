from collections import Counter

class Solution:
    
    def rec(self, cursum, target, a, cand, n, ans, idx):
        if cursum == target:
            b = sorted(a.copy())
            if b not in ans:
                ans.append(b)
            return
        else:
            for i in range(idx, n):
                a.append(cand[i])
                cursum += cand[i]
                if cursum <= target:
                    self.rec(cursum, target, a, cand, n, ans, idx + 1)
                cursum -= cand[i]
                a.pop()
                
    def check(self, a, b):
        d1 = Counter(a)
        d2 = Counter(b)
        for i in d2:
            if d2[i] > d1[i]:
                return False
        return True
            
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        a = []        
        if sum(candidates) < target:
            return []
        if len(set(candidates)) == 1 and target % candidates[0] == 0:
                return [[candidates[0]] * (target // candidates[0])]
        self.rec(0, target, a, candidates, n, ans, 0)     
        return [i for i in ans if self.check(candidates, i)]

    