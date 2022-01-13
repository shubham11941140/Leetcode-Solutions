class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        # Pick max of each entry and greedily select all
        # Once no more can be picked shoot next arrow
        print(points)
        n = len(points)
        i = 0
        ans = 0
        f = -(10 ** 100)
        while i < n:
            f = points[i][1]
            c = 0
            while i < n and points[i][0] <= f <= points[i][1]:
                i += 1
                c = 1
            ans += 1
            print(f)
            if not c:
                i += 1            
        return ans
        