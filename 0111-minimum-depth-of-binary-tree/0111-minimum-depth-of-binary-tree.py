# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def replace(self, root):
        if root is None:
            return
        else:
            root.val = 1
            self.replace(root.left)
            self.replace(root.right)

    def rtols(self, root, a, v):
        v += root.val
        if root.left is None and root.right is None:
            a.append(v)
        else:
            if root.left:
                self.rtols(root.left, a, v)
            if root.right:
                self.rtols(root.right, a, v)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        a = []
        v = 0
        self.replace(root)
        if root is not None:
            self.rtols(root, a, v)
        return 0 if not a else min(a)
