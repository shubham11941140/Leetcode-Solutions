# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def same(self, root1, root2):
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (root1 and not root2):
            return False
        if root1.val == root2.val:
            return self.same(root1.left, root2.left) and self.same(root1.right, root2.right)
        return False
    
    
    def flip(self, root1, r):
        if not root1:
            return
        r.val = root1.val
        if root1.right and not r.left:
            r.left = TreeNode()
            self.flip(root1.right, r.left)
        if root1.left and not r.right:
            r.right = TreeNode()
            self.flip(root1.left, r.right)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        r = TreeNode()
        self.flip(root, r)        
        return self.same(root, r)

                
            

        