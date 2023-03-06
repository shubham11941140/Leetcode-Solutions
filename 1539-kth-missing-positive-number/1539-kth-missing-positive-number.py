class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = 0
        for i in range(1, arr[-1] + k + 1):
            if i not in arr:
                missing += 1
            if missing == k:
                return i
