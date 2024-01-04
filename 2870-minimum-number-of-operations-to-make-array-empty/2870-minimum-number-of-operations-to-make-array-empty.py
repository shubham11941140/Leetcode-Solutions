class Solution:    
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        if 1 in c.values():
            return -1
        else:
            ans = 0
            for i in c:
                rem = c[i] % 6
                op = c[i] // 6
                if rem == 0:
                    ans += (2 * op)
                if rem in [1, 2, 3]:
                    ans += (2 * op + 1)
                if rem in [4, 5]:
                    ans += (2 * op + 2)
            return ans
                    
                
        
       