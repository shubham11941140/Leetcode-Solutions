class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        f = Counter(nums)
        m = max(f.values())
        print(f, m)
        a = []
        for c in range(1, m + 1):
            b = []
            for i in f:
                if c <= f[i]:
                    b.append(i)
            a.append(b)
        return a
                    
                
            
              