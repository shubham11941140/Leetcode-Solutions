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

        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result
