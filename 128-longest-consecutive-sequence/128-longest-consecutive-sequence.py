class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = sorted(list(set(nums)))
        n = len(a)
        b = [-1] + [i for i in range(n - 1) if a[i + 1] != a[i] + 1] + [n - 1]
        return max([(b[i + 1] - b[i]) for i in range(len(b) - 1)])
                
        