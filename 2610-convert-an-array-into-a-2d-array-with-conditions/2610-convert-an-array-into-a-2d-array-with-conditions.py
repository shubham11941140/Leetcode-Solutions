class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        f = Counter(nums)
        m = max(f.values())
        return [[i for i in f if c <= f[i]] for c in range(1, m + 1)]
                    
                
            
              