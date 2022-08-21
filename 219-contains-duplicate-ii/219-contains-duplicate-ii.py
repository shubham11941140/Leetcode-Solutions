class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        for i, item in enumerate(nums):
            if item in d:
                d[item].append(i)
            else:
                d[item] = [i]
        for i in d:
            if len(d[i]) > 1:
                l = d[i].copy()
                for i in range(len(l) - 1):
                    if l[i + 1] - l[i] <= k:
                        return True
        return False
