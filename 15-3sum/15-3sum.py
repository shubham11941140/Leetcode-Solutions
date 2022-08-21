class Solution:
        
    def compute(self, nums, n, ans):
        for i in range(n):
            val = -(nums[i])
            left = i + 1
            right = n - 1  
            while left < right:
                t = nums[left] + nums[right]
                if t == val:
                    if i not in (left, right):
                        b = sorted([nums[i], nums[left], nums[right]])
                        ans.append(b)
                    left += 1
                    right -= 1
                elif t < val:
                    left += 1
                elif t > val:
                    right -= 1
        return ans
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        ans = []
        n = len(nums)
        t = self.compute(nums, n, ans)
        r = []
        for i in t:
            if i not in r:
                r.append(i)
        return r           
                        
        