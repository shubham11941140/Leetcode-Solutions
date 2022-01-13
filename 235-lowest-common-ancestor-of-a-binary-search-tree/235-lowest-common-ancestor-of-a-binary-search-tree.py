# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if seperate directions we have ans
        # else traverse till we reach there
        if not root:
            return root
        
        if root.val == p.val or root.val == q.val :
            return root
        
        if p.val == q.val:
            return p
        
        if p.val < root.val and q.val > root.val:
            return root
        
        if p.val > root.val and q.val < root.val:
            return root  
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)        