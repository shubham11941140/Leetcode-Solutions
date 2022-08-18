from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        n = len(arr)
        print(c)
        sc = dict(sorted(c.items(), key = lambda item: item[1], reverse = True))
        print(sc)
        s = 0
        ans = []
        for i in sc:
            s += sc[i]
            ans.append(i)
            print(i, sc[i])
            if s >= n // 2:
                break
        print(ans)
        return len(ans)
        