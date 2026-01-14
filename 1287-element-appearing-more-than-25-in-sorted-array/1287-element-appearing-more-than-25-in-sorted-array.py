class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = Counter(arr)
        n = len(arr)
        for i in c:
            if c[i] > n // 4:
                return i
