class Solution:

    def binary_search(self, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if self.even[mid] == x:
                return mid
            elif self.even[mid] > x:
                return self.binary_search(low, mid - 1, x)
            else:
                return self.binary_search(mid + 1, high, x)
        return -1

    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cz = changed.count(0)
        if cz % 2:
            return []
        ans = [0 for i in range(cz // 2)]
        changed = [i for i in changed if i]
        self.even = sorted([i for i in changed if i % 2 == 0])
        le = len(self.even)
        odd = [i for i in changed if i % 2]
        for i in odd:
            bs = self.binary_search(0, le - 1, 2 * i)
            if bs != -1:
                del self.even[bs]
                le -= 1
            else:
                return []
        if le % 2:
            return []
        else:
            ans += odd
            while self.even:
                m = self.even[0]
                bs = self.binary_search(0, le - 1, 2 * m)
                if bs != -1:
                    ans += [m]
                    del self.even[bs]
                    del self.even[0]
                    le -= 2
                else:
                    return []
        return ans
