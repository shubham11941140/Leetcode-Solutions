"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
        
    def postorder_nary(self, root, a):
        if root is None:
            return
        for i in root.children:
            self.postorder_nary(i, a)
        a.append(root.val)
    
    def postorder(self, root: 'Node') -> List[int]:
        a = []
        self.postorder_nary(root, a)
        return a
        