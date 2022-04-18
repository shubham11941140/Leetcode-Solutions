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
    
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        a = []
        self.inorder(root, a)
        print(a)
        m = min(a)
        while m in a:
            a.remove(m)
        print(a)
        if not a:
            return -1
        else:
            return min(a)
        