class Solution:
    @staticmethod
    def countGoodTriplets(arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        c2 = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        c2 += 1
        return c2
