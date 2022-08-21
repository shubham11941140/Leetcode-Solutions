# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def roottoleafsum(self, root, a, val):
        val += root.val
        if root.left is None and root.right is None:
            a.append(val)
        else:            
            if root.left:
                self.roottoleafsum(root.left, a, val)
            if root.right:
                self.roottoleafsum(root.right, a, val)
                
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        a = []
        val = 0
        if root is not None:
            self.roottoleafsum(root, a, val)
        return targetSum in a
