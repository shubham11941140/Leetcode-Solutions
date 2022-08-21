# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder(self, root, a):
        if root is None:
            return
        self.inorder(root.left, a)
        a.append(root.val)
        self.inorder(root.right, a)

    @staticmethod
    def reconstruct(a, n):
        c = TreeNode()
        b = c
        for i in range(n):
            b.val = a[i]
            if i < n - 1:
                b.right = TreeNode()
                b = b.right
        return c

    def insertIntoBST(self, root: Optional[TreeNode],
                      val: int) -> Optional[TreeNode]:
        a = [val]
        self.inorder(root, a)
        return self.reconstruct(sorted(a), len(a))
