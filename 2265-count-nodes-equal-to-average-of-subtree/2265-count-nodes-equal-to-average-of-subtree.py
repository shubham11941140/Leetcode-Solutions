# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def avg(self, root, s, co):
        if not root:
            return
        s += root.val
        co += 1
        self.avg(root.left, s, co)
        self.avg(root.right, s, co)  
    
    def croot(self, root):
        if not root:
            return
        s = 0
        co = 0
        self.avg(root, s, co)
        if co and s // co == root.val:
            self.c += 1
        self.croot(root.left)
        self.croot(root.right)
        
        
    def rsum(self, root):
        if not root:
            return
        self.ans1 += root.val
        self.ans2 += 1
        #print(34, self.ans1, self.ans2)
        if root.left:
            self.rsum(root.left)
        if root.right:
            self.rsum(root.right)
        
    def call(self, root):
        if not root:
            return
        self.ans1 = 0
        self.ans2 = 0
        self.rsum(root)
        if self.ans2:
            if root.val == (self.ans1 // self.ans2):
                self.c += 1
        #if root.left:            
        self.call(root.left)
        #if root.right:            
        self.call(root.right)
        
                    
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.c = 0
        self.call(root)
        return self.c
        