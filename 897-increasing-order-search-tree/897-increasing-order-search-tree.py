# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.a = []
    
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.a.append(root.val)
        self.inorder(root.right)
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.inorder(root)
        new_root = TreeNode(self.a[0])
        new_root_copy = new_root
        for i in range(1, len(self.a)):
            new_root.right = TreeNode(self.a[i])
            new_root = new_root.right
        return new_root_copy
        