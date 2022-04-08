class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kl = sorted(nums, reverse = True)
        self.k = k - 1
        
    def add(self, val: int) -> int:
        self.kl += [val]
        self.kl.sort(reverse = True)
        return self.kl[self.k]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)