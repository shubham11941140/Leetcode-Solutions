class Solution:
    
    def rec(self, idx, a, ans):
        if idx == len(a):
            ans.append(a.copy())
        for i in range(idx, len(a)):
            a[i], a[idx] = a[idx], a[i]
            self.rec(idx + 1, a, ans)
            a[idx], a[i] = a[i], a[idx]
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.rec(0, nums, ans)
        return ans
        