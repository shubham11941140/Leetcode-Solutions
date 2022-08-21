class Solution:

    @staticmethod
    def freq(arr):
        d = {}
        for i in arr:
            d[i] = d[i] + 1 if i in d else 1
        return d

    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = []
        s = list(set(arr))
        n = len(s)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if s[i] + s[j] + s[k] == target:
                        tup = sorted([s[i], s[j], s[k]])
                        if tup not in ans:
                            ans.append(tup)
        f = self.freq(arr)
        c = 0
        for x, y, z in ans:
            if x == y == z:
                c += (f[x] * (f[x] - 1) * (f[x] - 2)) // 6
            elif x == y and y != z:
                c += ((f[x] * (f[x] - 1)) // 2) * f[z]
            elif x != y and y == z:
                c += ((f[y] * (f[y] - 1)) // 2) * f[x]
            else:
                c += f[x] * f[y] * f[z]
        return c % (10**9 + 7)
