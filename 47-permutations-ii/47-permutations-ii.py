class Solution:
    
    def permute(self, idx, a, ans):
        if idx == len(a):
            if a not in ans:
                ans.append(a.copy())
        for i in range(idx, len(a)):
            a[i], a[idx] = a[idx], a[i]
            self.permute(idx + 1, a, ans)
            a[idx], a[i] = a[i], a[idx]   
            
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.permute(0, nums, ans)
        return ans        
