class Solution:
    def dist(self, p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])    
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        n = len(trees)
        if n < 4:
            return trees
        trees.sort()
        hull = []
        for p in trees:
            while len(hull) >= 2 and self.dist(hull[-2], hull[-1], p) < 0:
                hull.pop()
            hull.append(p)
        for p in reversed(trees):
            while len(hull) >= 2 and self.dist(hull[-2], hull[-1], p) < 0:
                hull.pop()
            hull.append(p)
        return list(set(map(tuple, hull)))