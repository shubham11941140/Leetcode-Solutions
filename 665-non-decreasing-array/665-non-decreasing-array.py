class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [i for i in range(n - 1) if nums[i] > nums[i + 1]]
        if not f:
            return True
        elif len(f) > 1:
            return False
        elif len(f) == 1:
            nums1 = nums.copy()
            nums2 = nums.copy()
            nums1[f[0]] = nums1[f[0] + 1]
            nums2[f[0] + 1] = nums2[f[0]]
            flag1 = True                        
            flag2 = True
            for i in range(n - 1):
                if nums1[i] > nums1[i + 1]:
                    flag1 = False
                    break                                        
            for i in range(n - 1):
                if nums2[i] > nums2[i + 1]:
                    flag2 = False
                    break
            return flag1 or flag2
