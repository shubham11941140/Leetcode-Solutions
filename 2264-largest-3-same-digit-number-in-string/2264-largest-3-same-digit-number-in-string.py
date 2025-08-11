class Solution:

    def largestGoodInteger(self, num: str) -> str:
        a = [str(i) * 3 for i in range(10)]
        n = len(num)
        b = [num[i:i + 3] for i in range(n - 2) if num[i:i + 3] in a]
        return max(b) if b else ""
