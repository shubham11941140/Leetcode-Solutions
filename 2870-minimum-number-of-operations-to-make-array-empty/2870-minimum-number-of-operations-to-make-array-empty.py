class Solution:    
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        if 1 in c.values():
            return -1
        else:
            ans = 0
            for i in c:
                rem = c[i] % 6 
                ans += (2 * (c[i] // 6))
                if rem in [1, 2, 3]:
                    ans += 1
                if rem in [4, 5]:
                    ans += 2
            return ans
                    
                
        
       