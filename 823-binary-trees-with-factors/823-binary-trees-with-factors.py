class Solution:

    @staticmethod
    def numFactoredBinaryTrees(arr: List[int]) -> int:
        M = 10**9 + 7
        n = len(arr)
        d = {}
        arr.sort()
        for i in arr:
            d[i] = 1
        for i in range(n):
            curr = arr[i]
            for j in range(i):
                mod = arr[j]
                if not curr % mod:
                    rem = curr // mod
                    if rem in d:
                        d[curr] = (d[curr] + (d[mod] * d[rem])) % M
        return sum(d.values()) % M
