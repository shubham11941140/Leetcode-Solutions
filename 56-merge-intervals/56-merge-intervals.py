class Solution:        
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        n = len(intervals)
        i = 0
        while i < n:
            s = intervals[i][0]
            e = intervals[i][1]
            while i + 1 < n and max(e, intervals[i][1]) >= intervals[i + 1][0]:
                if intervals[i][1] >= intervals[i + 1][0]:
                    e = max(e, intervals[i][1])
                i += 1
            e = max(e, intervals[i][1])
            ans.append([s, e])
            i += 1
        return ans
                
        