class Solution:

    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        n = len(strs)
        ans = ""
        for i in range(len(strs[0]) + 1):
            t = strs[0][:i]
            if len([j for j in range(1, n) if t == strs[j][:i]]) == n - 1:
                ans = t
        return ans
