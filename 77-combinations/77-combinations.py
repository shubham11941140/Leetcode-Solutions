from random import sample

class Solution:
    
    def gen(self, arr, k, a, idx, n, ans):
        if idx == n:
            if len(a) == k:
                ans.append(a.copy())
            return
        self.gen(arr, k, a + [arr[idx]], idx + 1, n, ans)
        self.gen(arr, k, a, idx + 1, n, ans)
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        l = list(range(1, n + 1))
        ans = []
        a = []
        self.gen(l, k, a, 0, n, ans)
        return ans
        