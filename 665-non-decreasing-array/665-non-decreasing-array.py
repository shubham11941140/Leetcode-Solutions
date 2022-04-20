class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        f = []
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                f.append(i)
        print(f)
        if not f:
            return True
        elif len(f) > 1:
            return False
        elif len(f) == 1:
            # Check whether we can acheive
            nums1 = nums.copy()
            nums1[f[0]] = nums1[f[0] + 1]
            flag1 = True
            for i in range(n - 1):
                if nums1[i] > nums1[i + 1]:
                    flag1 = False
                    
                    
            nums2 = nums.copy()
            nums2[f[0] + 1] = nums2[f[0]]
            flag2 = True
            for i in range(n - 1):
                if nums2[i] > nums2[i + 1]:
                    flag2 = False
            return flag2 or flag1
            
        # return True if len(f) == 1 else False
        