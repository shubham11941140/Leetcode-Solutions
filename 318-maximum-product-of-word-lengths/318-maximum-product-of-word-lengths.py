class Solution:

    @staticmethod
    def maxProduct(words: List[str]) -> int:
        n = len(words)
        s = [set(i) for i in words]
        l = [len(i) for i in words]
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if s[i].intersection(s[j]) == set():
                    val = l[i] * l[j]
                    ans = max(ans, val)
        return ans
