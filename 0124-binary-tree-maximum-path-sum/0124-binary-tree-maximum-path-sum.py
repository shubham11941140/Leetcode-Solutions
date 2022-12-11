# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def p(self, root):
        if root is None:
            return -50
        l = self.p(root.left)
        r = self.p(root.right)
        self.r[root.val] = root.val + sum([k for k in [l, r] if k > 0])
        return max(root.val, root.val + max(l, r))

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.r = [-50] * (10**5)
        self.p(root)
        return max(self.r)
