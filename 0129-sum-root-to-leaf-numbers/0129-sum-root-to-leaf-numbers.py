# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rs(self, root, val):
        val += str(root.val)
        if root.left is None and root.right is None:
            self.a.append(val)
        else:
            if root.left:
                self.rs(root.left, val)
            if root.right:
                self.rs(root.right, val)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.a = []
        val = ""
        self.rs(root, val)
        return sum([int(i) for i in self.a])
