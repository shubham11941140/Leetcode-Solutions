from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        d = Counter(nums)
        return [y for x, y in sorted([(d[i], i) for i in d], reverse = True)[:k]]
