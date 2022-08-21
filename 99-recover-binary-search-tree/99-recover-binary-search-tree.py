# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.a = []

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.a.append(root.val)
        self.inorder(root.right)

    def modify(self, root, x, y):
        if root is None:
            return
        if root.val == x:
            self.xval = root
        if root.val == y:
            self.yval = root
        self.modify(root.left, x, y)
        self.modify(root.right, x, y)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        b = sorted(self.a)
        n = len(b)
        for i in range(n):
            if self.a[i] != b[i]:
                x, y = self.a[i], b[i]
                break
        self.modify(root, x, y)
        self.xval.val = y
        self.yval.val = x
