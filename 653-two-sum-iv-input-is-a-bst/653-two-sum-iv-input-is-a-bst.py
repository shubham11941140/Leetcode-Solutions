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
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        a = []
        self.inorder(root, a)
        n = len(a)
        for i in range(n):
            if k - a[i] in a and a[i] != k - a[i]:
                return True
        return False
        