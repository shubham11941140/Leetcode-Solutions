class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        ce = len([i for i in range(n) if nums1[i] % 2 == 0])
        co = n - ce
        if ce == n or co == n:
            return True
        nums1.sort()
        if nums1[0] % 2 == 0:
            return False
        return True

        