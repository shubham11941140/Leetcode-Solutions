class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.pre = [0 for i in range(n)]
        self.pre[0] = nums[0]
        for i in range(1, n):
            self.pre[i] = self.pre[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right] - self.pre[left -
                                          1] if left else self.pre[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
