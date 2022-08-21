class Solution:
    
    def can(self, y, x):
        a, b = x
        c, d = y
        return c <= a and b <= d                
    
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        #print(intervals)
        while True:
            #print(intervals)
            cur = len(intervals)
            for i in range(len(intervals) - 1):
                if self.can(intervals[i], intervals[i + 1]):
                    intervals.remove(intervals[i + 1])
                    break
                elif self.can(intervals[i + 1], intervals[i]):
                    intervals.remove(intervals[i])
                    break
            nex = len(intervals)
            if cur ==  nex:
                break
        return len(intervals)
                    
                
