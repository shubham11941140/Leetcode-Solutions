class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        f = Counter(nums)
        m = max(f.values())
        a = []
        for c in range(1, m + 1):
            b = [i for i in f if c <= f[i]]
            a.append(b)
        return a
