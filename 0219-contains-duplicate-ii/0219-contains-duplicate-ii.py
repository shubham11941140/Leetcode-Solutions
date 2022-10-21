class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import defaultdict
        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)
        for i in d:
            if len(d[i]) > 1:
                for j in range(len(d[i]) - 1):
                    if d[i][j + 1] - d[i][j] <= k:
                        return True
        return False
            
        
        