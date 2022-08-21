from random import randint


class Solution:

    def __init__(self, nums: List[int]):
        self.a = nums
        self.n = len(nums)

    def pick(self, target: int) -> int:
        idxa = [i for i in range(self.n) if self.a[i] == target]
        return idxa[randint(0, len(idxa) - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
