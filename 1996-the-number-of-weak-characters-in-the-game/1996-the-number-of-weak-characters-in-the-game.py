import bisect


class Solution:

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:

        # dict mapping
        # optimal move
        """
        c = dict()
        for a, d in properties:
            if a not in c:
                c[a] = [d]
            else:
                bisect.insort(c[a], d)
        print(c)
        """

        properties.sort()
        n = len(properties)
        ans = 0
        # print(properties)
        maxa = [0] * n
        maxa[n - 1] = properties[-1][1]
        for i in reversed(range(n - 1)):
            maxa[i] = max(properties[i][1], maxa[i + 1])
        # print(maxa)
        for i in range(n):
            a, d = properties[i]
            for j in range(i + 1, n):
                if properties[j][0] > a:
                    # print(maxa[j], maxa[j] > d)
                    if maxa[j] > d:
                        ans += 1
                    break
        return ans
