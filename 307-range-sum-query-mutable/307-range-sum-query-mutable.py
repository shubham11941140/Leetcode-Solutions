class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.s = sum(nums)
        self.l = len(nums) // 2
        
    def update(self, index: int, val: int) -> None:
        self.s += (val - self.nums[index])
        self.nums[index] = val        
        
    def sumRange(self, left: int, right: int) -> int:
        return self.s - (sum(self.nums[:left]) + sum(self.nums[right + 1:])) if right - left > self.l else sum(self.nums[left:right + 1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
