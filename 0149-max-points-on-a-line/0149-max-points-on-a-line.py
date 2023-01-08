class Solution:    
    
    def equ(self, p1, p2):
        n = p1[1] - p2[1]
        d = p1[0] - p2[0]
        if not d:
            return 10 ** 15, 10 ** 15
        a = n / d
        c =  p1[1] - (a * p1[0])
        return a, c

    def lies(self, a, c, p):
        return abs(p[1] - (a * p[0] + c)) < 10 ** (-5)

    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        max_points = 0
        for i in range(len(points)):
            slope_dict = {}
            same_points = 1
            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same_points += 1
                    continue
                slope = self.slope(points[i], points[j])
                if slope in slope_dict:
                    slope_dict[slope] += 1
                else:
                    slope_dict[slope] = 1
            if len(slope_dict) == 0:
                max_points = max(max_points, same_points)
            else:
                max_points = max(max_points, max(slope_dict.values()) + same_points)
        return max_points

    def slope(self, p1, p2):
        if p1[0] == p2[0]:
            return 'inf'
        return (p1[1] - p2[1]) / (p1[0] - p2[0])
                        
        