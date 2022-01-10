class Solution:        
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        ans = []
        n = len(intervals)
        i = 0
        while i < n:
            # Merge loop
            s = intervals[i][0]
            e = intervals[i][1]
            c = 0
            while i + 1 < n and max(e, intervals[i][1]) >= intervals[i + 1][0]:
                c = 1
                print(i)      
                if intervals[i][1] >= intervals[i + 1][0]:
                    # Full overlap
                    e = max(e, intervals[i][1])
                    #i += 1
                i += 1
                
            print(i)
            e = max(e, intervals[i][1])
            print([s, e])
            ans.append([s, e])
            #if not c:
            i += 1
        return ans
                
        