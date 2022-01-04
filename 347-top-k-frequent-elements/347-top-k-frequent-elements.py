from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        d = Counter(nums)
        a = [(d[i], i) for i in d]
        v = sorted(a, reverse = True)
        return [i[1] for i in v[:k]]