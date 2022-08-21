# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def postorder(self, root, a):
        if root is None:
            return
        self.postorder(root.left, a)
        self.postorder(root.right, a)
        a.append(root.val)
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a = []
        self.postorder(root, a)
        return a
        
