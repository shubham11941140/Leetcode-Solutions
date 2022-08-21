class Solution:

    @staticmethod
    def Counter(arr):
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return d

    def fourSumCount(self, nums1: List[int], nums2: List[int],
                     nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        a = []
        b = []
        for i in range(n):
            for j in range(n):
                v = nums1[i] + nums2[j]
                a.append(v)
        for i in range(n):
            for j in range(n):
                v = nums3[i] + nums4[j]
                b.append(v)

        d1 = self.Counter(a)
        d2 = self.Counter(b)
        c = 0
        for i in d1:
            for j in d2:
                if i + j == 0:
                    c += d1[i] * d2[j]
        return c
