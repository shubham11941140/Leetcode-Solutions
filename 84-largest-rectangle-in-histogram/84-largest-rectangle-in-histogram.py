class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = -1
        n = len(heights)
        l = [-1] * n
        r = [n] * n
        ls = []
        rs = []
        for i in range(n):
            while ls and heights[i] <= ls[-1][0]:
                ls.pop()
            if ls:
                l[i] = ls[-1][1]            
            ls.append((heights[i], i))            
        for i in reversed(range(n)):
            while rs and heights[i] <= rs[-1][0]:
                rs.pop()
            if rs:
                r[i] = rs[-1][1]            
            rs.append((heights[i], i))       
        for i in range(n):
            ans = max(ans, heights[i] * (r[i] - l[i] - 1))
        return ans
        