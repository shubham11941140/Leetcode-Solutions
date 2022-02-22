# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.ansarr = []        
    
    def present(self, root, key):
        if not root:
            return False
        if root.val == key:
            return True
        return self.present(root.left, key) or self.present(root.right, key)    
    
    def findpath(self, root, p, ans1):
        if not root:
            return False
        if root.val == p.val:
            ans1.append(root)
            return True
        if self.findpath(root.left, p, ans1) or self.findpath(root.right, p, ans1):
            ans1.append(root)
        return False
    
    def call(self, root, p, q):
        if not root:
            return root
        LP = self.present(root.left, p.val)
        RP = self.present(root.right, p.val)
        LQ = self.present(root.left, q.val)
        RQ = self.present(root.right, q.val)
        if (LP and RQ) or (LQ and RP):
            self.ansarr.append(root)
            return root
        elif LP and LQ:
            self.ansarr.append(root.left)
            return self.call(root.left, p, q)
        elif RP and RQ:
            self.ansarr.append(root.right)
            return self.call(root.right, p, q)        
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':       
        if max(p.val, q.val) < 1500:
            self.call(root, p, q)        
            return root if not self.ansarr else self.ansarr[-1]        
        ansp = []
        self.findpath(root, p, ansp)
        ansq = []
        self.findpath(root, q, ansq)
        ansp = ansp[::-1]
        ansq = ansq[::-1]
        i = 0
        while i < min(len(ansp), len(ansq)) and ansp[i].val == ansq[i].val:
            i += 1 
        return ansp[i - 1]        
        
        
        