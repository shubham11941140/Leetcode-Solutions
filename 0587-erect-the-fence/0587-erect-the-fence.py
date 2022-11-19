class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        points = trees.copy()
        n = len(points)
        if n < 4:
            return points
        points.sort(key=lambda x: (x[0], x[1]))
        def ccw(p1, p2, p3):
            return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
        hull = []
        for i in range(n):
            while len(hull) >= 2 and ccw(hull[-2], hull[-1], points[i]) < 0:
                hull.pop()
            hull.append(points[i])
        for i in reversed(range(n)):
            while len(hull) >= 2 and ccw(hull[-2], hull[-1], points[i]) < 0:
                hull.pop()
            hull.append(points[i])
        return list(set(map(tuple, hull)))