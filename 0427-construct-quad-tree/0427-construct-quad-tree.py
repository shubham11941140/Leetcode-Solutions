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
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(grid):
            n = len(grid)
            if n == 1:
                return Node(grid[0][0], True, None, None, None, None)
            else:
                a = dfs([row[:n//2] for row in grid[:n//2]])
                b = dfs([row[n//2:] for row in grid[:n//2]])
                c = dfs([row[:n//2] for row in grid[n//2:]])
                d = dfs([row[n//2:] for row in grid[n//2:]])
                if a.isLeaf and b.isLeaf and c.isLeaf and d.isLeaf and a.val == b.val == c.val == d.val:
                    return Node(a.val, True, None, None, None, None)
                else:
                    return Node(0, False, a, b, c, d)
        return dfs(grid)        