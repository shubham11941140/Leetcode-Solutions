from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        sc = dict(sorted(Counter(arr).items(), key = lambda item: item[1], reverse = True))
        s = 0
        ans = 0
        for i in sc:
            s += sc[i]
            ans += 1
            if s >= n // 2:
                break
        return ans
