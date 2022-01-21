class Solution:
    
    def rec(self, cursum, target, a, cand, n, ans):
        if cursum == target:
            b = sorted(a.copy())
            if b not in ans:
                ans.append(b)
            return
        else:
            for i in range(n):
                a.append(cand[i])
                cursum += cand[i]
                if cursum <= target:
                    self.rec(cursum, target, a, cand, n, ans)
                cursum -= cand[i]
                a.pop()
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        a = []
        self.rec(0, target, a, candidates, n, ans)
        return ans
        