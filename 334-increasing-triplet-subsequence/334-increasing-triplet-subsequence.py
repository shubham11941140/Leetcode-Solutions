class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:        
        n = len(nums)        
        MIN = 10 ** 100
        MAX = -1 * (10 ** 100)
        st = [[0 for i in range(n)] for j in range(3)]
        for i in range(n):
            if nums[i] < MIN:
                MIN = nums[i]
            st[0][i] = MIN
            st[1][i] = nums[i]
        for i in reversed(range(n)):
            if nums[i] > MAX:
                MAX = nums[i]
            st[2][i] = MAX
        for i in range(n):
            if st[0][i] < st[1][i] < st[2][i]:
                return True        
        return False
            
        