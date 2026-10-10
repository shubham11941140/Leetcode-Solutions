class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        k = k1 + k2
        counter = Counter(diff)
        maxDiff = max(counter.keys())
        for val in range(maxDiff, 0, -1):
            if k <= 0:
                break
            sub = min(k, counter[val])
            counter[val] -= sub
            counter[val - 1] += sub
            k -= sub
        return sum([(d**2) * v for d, v in counter.items()])