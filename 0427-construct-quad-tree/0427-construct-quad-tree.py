"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:

    def dfs(self, grid):
        n = len(grid)
        if n == 1:
            return Node(grid[0][0], True, None, None, None, None)
        else:
            a = self.dfs([row[:n // 2] for row in grid[:n // 2]])
            b = self.dfs([row[n // 2:] for row in grid[:n // 2]])
            c = self.dfs([row[:n // 2] for row in grid[n // 2:]])
            d = self.dfs([row[n // 2:] for row in grid[n // 2:]])
            return (Node(a.val, True, None, None, None, None)
                    if a.isLeaf and b.isLeaf and c.isLeaf and d.isLeaf
                    and a.val == b.val == c.val == d.val else Node(
                        0, False, a, b, c, d))

    def construct(self, grid: List[List[int]]) -> "Node":
        return self.dfs(grid)
