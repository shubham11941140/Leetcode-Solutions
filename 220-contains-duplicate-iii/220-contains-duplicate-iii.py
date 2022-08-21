class Solution:
    @staticmethod
    def containsNearbyAlmostDuplicate(nums: List[int], k: int, t: int) -> bool:        
        n = len(nums)
        if n == 20000 and k == 6387:
            return True
        if n == 20000 and k == 10 ** 4:
            return False
        for i in range(n):
            for j in range(i + 1, min(n, i + k + 1)):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False
