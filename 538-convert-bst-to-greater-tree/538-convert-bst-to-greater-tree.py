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

    def modify(self, root, d):
        if root is None:
            return
        self.modify(root.left, d)
        root.val += d[root.val]
        self.modify(root.right, d)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        a = []
        self.inorder(root, a)
        n = len(a)
        pre = [0] * n
        pre[0] = a[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + a[i]
        s = sum(a)
        d = {}
        for i in range(n):
            d[a[i]] = s - pre[i]
        self.modify(root, d)
        return root
