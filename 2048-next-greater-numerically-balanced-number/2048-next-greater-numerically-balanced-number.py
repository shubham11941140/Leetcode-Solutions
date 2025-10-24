class Solution:

    def nextBeautifulNumber(self, n: int) -> int:
        i = n + 1
        while True:
            c = Counter(str(i))
            f = True
            for j in c:
                if int(j) != c[j]:
                    f = False
                    break
            if f:
                return i
            i += 1
