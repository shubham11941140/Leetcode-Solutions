class Solution:

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        a = sorted(arr)
        arr = [a[k + 1] - a[k] for k in range(len(a) - 1)]
        return min(arr) == max(arr)
