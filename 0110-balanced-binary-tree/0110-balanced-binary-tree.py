# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def height(self, root):
        return (0 if root is None else 1 +
                max(self.height(root.left), self.height(root.right)))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            return (False
                    if abs(self.height(root.left) -
                           self.height(root.right)) > 1 else
                    self.isBalanced(root.left) and self.isBalanced(root.right))
