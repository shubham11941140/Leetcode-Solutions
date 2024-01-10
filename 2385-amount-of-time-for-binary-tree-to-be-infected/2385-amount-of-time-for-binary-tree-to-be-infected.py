# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
       
    def cp(self, root):
        if root.val == self.s:
            self.r = root        
        for i in [root.left, root.right]:
            if i:
                self.p[i.val] = root
                self.cp(i)              
    
    def bfs(self, r):
        q = [(r, 0)]
        s = set()
        while q:
            root, level = q.pop(0)               
            if not root or root.val in s:
                continue
            self.m = max(self.m, level)
            s.add(root.val)
            if root.left:
                q.append((root.left, level + 1))
            if root.right:
                q.append((root.right, level + 1))  
            if root.val in self.p:
                q.append((self.p[root.val], level + 1))
                    
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.p = dict()
        self.s = start
        self.cp(root)
        self.m = 0
        self.bfs(self.r)        
        return self.m                