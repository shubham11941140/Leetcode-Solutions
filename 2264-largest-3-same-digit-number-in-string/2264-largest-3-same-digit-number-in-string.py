class Solution:

    def largestGoodInteger(self, num: str) -> str:
        a = [str(i) * 3 for i in range(10)]
        n = len(num)
        b = []
        for i in range(n - 2):
            print(num[i:i + 3])
            if num[i:i + 3] in a:
                b.append(num[i:i + 3])
        return max(b) if b else ""
