# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def leafvalue(self, root, a):
        if not root:
            return
        if not root.left and not root.right:
            a.append(root.val)
        self.leafvalue(root.left, a)
        self.leafvalue(root.right, a)                        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a = []
        b = []
        self.leafvalue(root1, a)
        self.leafvalue(root2, b)
        return a == b
        
