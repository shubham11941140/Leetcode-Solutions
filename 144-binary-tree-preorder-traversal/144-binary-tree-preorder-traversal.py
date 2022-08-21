# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preorder(self, root, a):
        if root is None:
            return
        a.append(root.val)
        self.preorder(root.left, a)
        self.preorder(root.right, a)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a = []
        self.preorder(root, a)
        return a            