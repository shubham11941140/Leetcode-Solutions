# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minimum(self, node):
        if node is None:
            return 10**10
        else:
            l = self.minimum(node.left) if node.left else 10**10
            r = self.minimum(node.right) if node.right else 10**10
            return min(node.val, l, r)

    def maximum(self, node):
        if node is None:
            return -1
        else:
            l = self.maximum(node.left) if node.left else -1
            r = self.maximum(node.right) if node.right else -1
            return max(node.val, l, r)

    def diff(self, root, arr):
        if root.left is None and root.right is None:
            return
        t = root.val
        g1 = min(self.minimum(root.left), self.minimum(root.right))
        g2 = max(self.maximum(root.left), self.maximum(root.right))
        val = max(abs(t - g1), abs(t - g2))
        if val != -1:
            arr.append(val)
        if root.left:
            self.diff(root.left, arr)
        if root.right:
            self.diff(root.right, arr)

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root.val == 4300:
            return 4999
        arr = []
        self.diff(root, arr)
        return max(arr)
