class Solution:

    def helper(self, arr, index, s):
        if index == len(arr):
            return len(s)
        res = 0
        if len(set(s + arr[index])) == len(s + arr[index]):
            res = max(res, self.helper(arr, index + 1, s + arr[index]))
        res = max(res, self.helper(arr, index + 1, s))
        return res

    def maxLength(self, arr: List[str]) -> int:
        res = []
        for i in arr:
            if len(set(i)) == len(i):
                res.append(i)
        return self.helper(res, 0, "")
