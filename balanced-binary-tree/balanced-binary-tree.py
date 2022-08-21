# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def balanced(self, root):
        if root is None:
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)
        if abs(lh - rh) > 1:
            return False
        return self.balanced(root.left) and self.balanced(root.right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.balanced(root)
