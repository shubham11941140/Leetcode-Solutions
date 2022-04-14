# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def search(self, root, data):
        if root is None:
            return root
        if root.val == data:
            return root
        if root.val < data:
            return self.search(root.right, data)
        if root.val > data:
            return self.search(root.left, data)        
        
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.search(root, val)
        