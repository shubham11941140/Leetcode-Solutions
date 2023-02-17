# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  
    
    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []

    def minDiffInBST(self, root: TreeNode) -> int:
        a = self.inorder(root)
        return min(a[i + 1] - a[i] for i in range(len(a) - 1))      