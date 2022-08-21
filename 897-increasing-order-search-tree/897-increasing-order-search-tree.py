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
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        a = []
        self.inorder(root, a)
        new_root = TreeNode(a[0])
        new_root_copy = new_root
        for i in range(1, len(a)):
            new_root.right = TreeNode(a[i])
            new_root = new_root.right
        return new_root_copy
        
