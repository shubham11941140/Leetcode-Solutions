class Solution:
    
    def compute(self, nums, n, target):
        ans = 10 ** 10
        final = 10 ** 10
        for i in range(n):
            val = target - nums[i]
            left = i + 1
            right = n - 1  
            while left < right:
                t = nums[left] + nums[right]
                print(nums[i] + t)
                if t == val:
                    return target
                if t < val:
                    #ans = max(ans, nums[i] + t)
                    left += 1
                elif t > val:     
                    #ans = min(ans, nums[i] + t)
                    right -= 1
                if abs(t-val) < ans:
                    final = nums[i] + t
                    ans = abs(t-val)
                    print(final, ans)
        return final
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.compute(nums, len(nums), target)
        