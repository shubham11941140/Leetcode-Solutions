class Solution:  
    
    def long(self, arr, n, k):
        d = {}
        s = 0
        m = 0
        for i in range(n):
            s += arr[i]
            if s == k:
                m = i + 1
            elif s - k in d:
                m = max(m, i - d[s - k])
            if s not in d:
                d[s] = i
        return m    
            
    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)
        if x > s:
            return -1
        n = len(nums)
        if x == s:
            return n        
        l = self.long(nums, n, s - x)
        return -1 if not l else n - l        