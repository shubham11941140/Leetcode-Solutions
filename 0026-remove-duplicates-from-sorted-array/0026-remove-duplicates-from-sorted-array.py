class Solution:  
    def removeDuplicates(self, nums: List[int]) -> int:
        f = Counter(nums)
        for i in f:
            for _ in range(f[i]-1):
                nums.remove(i)
        return len(nums)
            
        