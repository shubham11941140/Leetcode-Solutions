"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
        
    def preorder_nary(self, root, a):
        if root is None:
            return
        a.append(root.val) 
        for i in root.children:
            self.preorder_nary(i, a)           
    
    def preorder(self, root: 'Node') -> List[int]:
        a = []
        self.preorder_nary(root, a)
        return a    