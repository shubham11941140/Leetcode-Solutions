# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rightmost(self, root):
        while root.right:
            root = root.right
        return root

    def flatten(self, root: Optional[TreeNode]) -> None:
        """Do not return anything, modify root in-place instead."""
        if root:
            nr = None
            rm = None
        while root:
            if root.left:
                rm = self.rightmost(root.left)
                nr = root.right
                root.right = root.left
                root.left = None
                rm.right = nr
            root = root.right
