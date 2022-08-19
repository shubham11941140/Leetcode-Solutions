from bisect import insort

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        d = {}
        for val in nums:
            if val - 1 in d and d[val - 1]:
                m = d[val - 1].pop(0)
                if val in d:
                    insort(d[val], m + 1)
                else:
                    d[val] = [m + 1]                
            else:
                if val in d:
                    insort(d[val], 1)       
                else:
                    d[val] = [1]
        for i in d:
            if d[i]:
                if d[i][0] < 3:
                    return False
        return True             
