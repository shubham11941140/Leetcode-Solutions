class Solution:
    
    def prefix(self, a):
        n = len(a)
        pre = [0 for i in range(n)]
        pre[0] = a[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + a[i]
        return pre
        
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # SW
        pre = self.prefix(nums)
        l = 0
        r = 0
        n = len(nums)
        a = set()
        ans = -1
        while r < n and l <= r:
            if nums[r] not in a:
                a.add(nums[r])
                r += 1
            elif nums[r] in a:
                a.remove(nums[l])
                l += 1
            #print(a, r, l)
            if l:
                s = pre[r - 1] - pre[l - 1]
            else:
                s = pre[r - 1]
            #print(s)
            ans = max(ans, s)
        return ans
            
                
                
        