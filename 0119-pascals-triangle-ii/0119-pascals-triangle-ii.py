class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a = [[] for i in range(35)]
        a[0].append(1)
        for i in range(1, 35):
            la = len(a[i - 1])
            a[i] += [
                sum([a[i - 1][k] for k in [j - 1, j] if 0 <= k < la]) for j in range(i)
            ]
        a.pop(0)
        return a[rowIndex]
