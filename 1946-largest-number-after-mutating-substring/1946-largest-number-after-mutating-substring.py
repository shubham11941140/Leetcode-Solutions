class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        n = len(num)
        res = []
        i = 0
        while i < n and change[int(num[i])] <= int(num[i]):
            res.append(num[i])
            i += 1
        while i < n and change[int(num[i])] >= int(num[i]):
            res.append(str(change[int(num[i])]))
            i += 1
        res += num[i:]
        return ''.join(res)        