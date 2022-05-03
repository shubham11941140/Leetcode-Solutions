class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # U + S
        # S + U + S
        # S + U
        n = len(nums)
        s = sorted(nums)
        print(nums,"\n", s)
        if s == nums:
            return 0
        l = 0
        r = n - 1
        while s[l] == nums[l]:
            l += 1
        while s[r] == nums[r]:
            r -= 1
        print(l, r)
        return r - l + 1
        
        
        
        
        
        # US
        ans = 10 ** 9
        for i in range(l):
            for j in range(i + 1, l):
                #print(nums[:i], nums[i:j], nums[j:])
                if nums[:i] + sorted(nums[i:j]) + nums[j:] == s:
                    ans = min(ans, len(nums[i:j]))
        return ans