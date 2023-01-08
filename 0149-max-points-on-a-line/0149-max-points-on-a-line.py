class Solution:    
    
    def slope(self, p1, p2):
        return 'inf' if p1[0] == p2[0] else (p1[1] - p2[1]) / (p1[0] - p2[0])

    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return n
        max_points = 0
        for i in range(n):
            slope_dict = {}
            same_points = 1
            for j in range(i + 1, n):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same_points += 1
                    continue
                slope = self.slope(points[i], points[j])
                slope_dict[slope] = slope_dict[slope] + 1 if slope in slope_dict else 1
            max_points = max(max_points, same_points + max(slope_dict.values()) if slope_dict else same_points)
        return max_points
                        
        