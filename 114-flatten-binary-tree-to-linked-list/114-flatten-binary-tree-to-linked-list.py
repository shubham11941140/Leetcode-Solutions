# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def pre(self, root):
        if not root:
            return
        self.a.append(root.val)
        self.pre(root.left)
        self.pre(root.right)
    
    def insert(self, item):
        t = ListNode(item)
        t.next = self.r
        self.r = t        
    
    def make(self, root, val):
        nn = TreeNode(val)
        nn.right = root
        nn.left = None
        root = nn
        return root
        
    def remove(self, root):
        if not root:
            return
        if root:
            self.remove(root.left)
            self.remove(root.right)
            print("Deleting node: ", root.val)
            print("B",root)
            root.left = None
            root.right = None
            root = None
            print("A",root)
        
    
    def rightmost(self, root):
        if root.right:
            return self.rightmost(root.right)
        return root
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            nr = None
            rm = None
        while root:
            if root.left:
                rm = self.rightmost(root.left);
                nr = root.right;
                root.right = root.left;
                root.left = None;
                rm.right = nr;
            root = root.right        
        
        


        