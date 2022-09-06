# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def subtree(self, root):
        if not root:
            return False
        q = [root]
        while q:
            root = q.pop(0)
            if root.val:
                return False                          
            q += [i for i in [root.left, root.right] if i]
        return True                               
        
    def rec(self, root):
        if not root:
            return
        if self.subtree(root.left):
            root.left = None
        if self.subtree(root.right):
            root.right = None        
        self.rec(root.left)
        self.rec(root.right)
    
    
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.rec(root)
        if not root.val and not root.left and not root.right:
                return None
        return root
        