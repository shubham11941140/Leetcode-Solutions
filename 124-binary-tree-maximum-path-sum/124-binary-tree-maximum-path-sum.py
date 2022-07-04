# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
        
    def path(self, root):
        if root is None:
            return -50
        l = self.path(root.left)
        r = self.path(root.right)
        tos = root.val
        tos += sum([k for k in [l, r] if k > 0])
        '''
        if l < 0 and r < 0:
            tos = max(tos, root.val)
        elif l < 0:
            tos = max(tos, root.val + r)
        elif r < 0:
            tos = max(tos, root.val + l)
        else:
            tos = max(tos, root.val + l + r)
        '''
        self.rooted[root.val] = tos
        return root.val if l < 0 and r < 0 else root.val + max(l, r)
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.rooted = [-50] * (10 ** 5)
        self.path(root)
        return max(self.rooted)
        
        
        
        