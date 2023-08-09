class Solution:
        
    def solve(self, nums, d, p):
        n = len(nums)
        c = 0
        i = 0
        while i < n - 1:
            if nums[i + 1] - nums[i] <= d:
                c += 1
                i += 1
            if c >= p:
                return True
            i += 1
        return False
    
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        lo, hi = 0, nums[n - 1] - nums[0]
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            n = len(nums)
            c = 0
            i = 0
            f = False
            while i < n - 1:
                if nums[i + 1] - nums[i] <= mid:
                    c += 1
                    i += 1
                if c >= p:
                    f = True
                i += 1     
            
            if f:
                hi = mid
            else:
                lo = mid + 1
        return lo
    