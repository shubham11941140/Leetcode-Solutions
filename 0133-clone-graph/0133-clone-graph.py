"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def __init__(self):
        self.v = {}

    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None
        if node in self.v:
            return self.v[node]
        cn = Node(node.val, [])
        self.v[node] = cn
        for i in node.neighbors:
            cn.neighbors.append(self.cloneGraph(i))
        return cn
