class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        mp = {}
        min_dist = float('inf')
        for i, curr in enumerate(nums):
            if curr in mp:
                min_dist = min(min_dist, i - mp[curr])
            rev = int(str(curr)[::-1])
            mp[rev] = i
        return -1 if min_dist == float('inf') else min_dist        