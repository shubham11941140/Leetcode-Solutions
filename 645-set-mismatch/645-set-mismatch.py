from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = list(range(1, len(nums) + 1))
        b = []
        d = Counter(nums)
        for i in d:
            if d[i] == 2:
                b.append(i)
                break
        for i in a:
            if i not in d:
                b.append(i)
                break
        return b