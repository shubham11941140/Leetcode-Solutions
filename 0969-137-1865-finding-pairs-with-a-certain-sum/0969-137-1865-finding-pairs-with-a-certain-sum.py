class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n1 = sorted(nums1)
        self.n = len(nums1)
        self.n2 = nums2
        self.c = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        cur = self.n2[index]
        self.n2[index] += val
        self.c[cur] -= 1
        self.c[cur + val] += 1

    def count(self, tot: int) -> int:
        return sum([
            self.c[tot - self.n1[i]] for i in range(self.n)
            if self.n1[i] <= tot and tot - self.n1[i] in self.c
        ])


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
