# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorder(self, root, a):
        if root is None:
            return
        self.inorder(root.left, a)
        a.append(root.val)
        self.inorder(root.right, a)
        
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a = []
        self.inorder(root, a)
        return a[k - 1]
        
