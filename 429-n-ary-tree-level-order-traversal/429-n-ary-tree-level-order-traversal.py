"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:

    @staticmethod
    def levelOrder(root: "Node") -> List[List[int]]:
        if root is None:
            return []
        a = [[] for i in range(10**5)]
        q = [(root, 0)]
        while q:
            r, level = q.pop(0)
            a[level].append(r.val)
            for i in r.children:
                q.append((i, level + 1))
        return [i for i in a if i]
