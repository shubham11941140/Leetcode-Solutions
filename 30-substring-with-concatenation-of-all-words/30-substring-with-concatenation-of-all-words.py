class Solution:

    @staticmethod
    def binarySearch(arr, x):
        l = 0
        r = len(arr)
        while l <= r:
            m = l + ((r - l) // 2)
            print(m)
            res = x == arr[m]
            if res == 0:
                return m - 1
            if res > 0:
                l = m + 1
            else:
                r = m - 1
        return -1

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words.sort()
        self.w = set(words)
        lwords = [len(i) for i in words]
        tlen = sum(lwords)
        lb = min(lwords)
        ub = max(lwords)
        ans = []
        for i in range(len(s)):
            b = s[i:i + tlen]
            idx = 0
            check = []
            while idx <= tlen:
                Flag = False
                for j in range(lb, ub + 1):
                    c = b[idx:idx + j]
                    if c in self.w:
                        # if self.binarySearch(words, c) != -1:
                        check.append(c)
                        idx += j
                        Flag = True
                        break
                if not Flag:
                    break
            if sorted(check) == words:
                ans.append(i)
        return ans
