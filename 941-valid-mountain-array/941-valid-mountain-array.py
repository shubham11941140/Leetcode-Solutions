class Solution:

    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        n = len(arr)
        if n < 3:
            return False
        f1 = False
        f2 = False
        while i < n - 1:
            if arr[i + 1] > arr[i]:
                i += 1
                f1 = True
            else:
                break
        while i < n - 1:
            if arr[i + 1] < arr[i]:
                i += 1
                f2 = True
            else:
                break
        return i == n - 1 and f1 and f2
