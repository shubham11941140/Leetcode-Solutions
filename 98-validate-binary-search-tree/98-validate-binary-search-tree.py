# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def smin(self, root):
        if not root:
            return 10**100
        return min(root.val, self.smin(root.left), self.smin(root.right))

    def smax(self, root):
        if not root:
            return -(10**100)
        return max(root.val, self.smax(root.left), self.smax(root.right))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if self.smin(root.right) > root.val > self.smax(root.left):
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        return False
