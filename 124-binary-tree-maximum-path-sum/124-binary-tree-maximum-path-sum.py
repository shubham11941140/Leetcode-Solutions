# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
        
    def path(self, root, rooted):
        if root is None:
            return -50
        l = self.path(root.left, rooted)
        r = self.path(root.right, rooted)
        tos = root.val
        if l < 0 and r < 0:
            tos = max(tos, root.val)
        elif l < 0:
            tos = max(tos, root.val + r)
        elif r < 0:
            tos = max(tos, root.val + l)
        else:
            tos = max(tos, root.val + l + r)
        rooted[root.val] = tos
        if l < 0 and r < 0:
            return root.val
        else:
            return root.val + max(l, r)
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        rooted = [-50] * (10 ** 5)
        self.path(root, rooted)
        return max(rooted)
        
        
        
        