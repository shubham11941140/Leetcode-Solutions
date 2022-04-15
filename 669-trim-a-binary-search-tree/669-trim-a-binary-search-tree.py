# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def change(self, root, low, high):
        if root is None:
            return
        if root.val < low or root.val > high:
            root.val = -1
        self.change(root.left, low, high)
        self.change(root.right, low, high)
    
    def make(self, root):
        if root is None:
            return
        if root.val != -1:
            if root.left and root.left.val == -1:
                print(22)
                if root.left.right and root.left.right.val != -1:
                    root.left = root.left.right
                    #root.left.left = None
                else:
                    root.left = None
            if root.right and root.right.val == -1:
                if root.right.left and root.right.left.val != -1:
                    root.right = root.right.left
                    #root.right.right = None
                else:
                    root.right = None
        elif root.val == -1:
            print(30)
            if root.left is None and root.right is None:
                root = None
        if root and root.left:
            self.make(root.left)
        if root and root.right:
            self.make(root.right)
    
    def trim(self, root, low, high):
        if root is None:
            return root
        root.left = self.trim(root.left, low, high)
        root.right = self.trim(root.right, low, high)
        if root.val < low:
            return root.right
        elif root.val > high:
            return root.left
        return root
        
    
    
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        print(root)
        if root is None:
            return root
        elif root:
            return self.trim(root, low, high)
        else:
            while root and root.val < low:
                root = root.right
            while root and root.val > high:
                print(root.val)
                root = root.left
        print(root)
        self.change(root, low, high)
        self.make(root)
        return root
        
        