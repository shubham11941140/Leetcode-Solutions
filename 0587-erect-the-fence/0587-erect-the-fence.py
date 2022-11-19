class Solution:

    def dist(self, p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] -
                                                                      p1[0])

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        n = len(trees)
        if n < 4:
            return trees
        # trees.sort(key = lambda x: (x[0], x[1]))
        trees.sort()
        hull = []
        for i in range(n):
            while len(hull) >= 2 and self.dist(hull[-2], hull[-1],
                                               trees[i]) < 0:
                hull.pop()
            hull.append(trees[i])
        for i in reversed(range(n)):
            while len(hull) >= 2 and self.dist(hull[-2], hull[-1],
                                               trees[i]) < 0:
                hull.pop()
            hull.append(trees[i])
        return list(set(map(tuple, hull)))
