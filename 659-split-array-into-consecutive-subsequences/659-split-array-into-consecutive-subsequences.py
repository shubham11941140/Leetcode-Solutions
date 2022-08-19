import bisect
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        d = {}
        for val in nums:
            if val - 1 in d and d[val - 1]:
                m = d[val - 1][0]
                if val in d:
                    bisect.insort(d[val], m + 1)
                    #d[val].append(m + 1)
                else:
                    d[val] = [m + 1]
                d[val - 1].pop(0)
            else:
                if val in d:
                    bisect.insort(d[val], 1)
                    #d[val].append(1)        
                else:
                    d[val] = [1]
        for i in d:
            if d[i]:
                mdi = min(d[i])
                if mdi < 3:
                    return False
        return True             
