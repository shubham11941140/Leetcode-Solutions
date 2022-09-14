# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import Counter, defaultdict

class Solution:            
    
    def rtl(self, root, d):
        if not root:
            return
        if not root.left and not root.right:
            d[root.val] += 1
            z = 0
            f = True
            for i in d.values():
                if i % 2 == 1:
                    z += 1
                if z > 1:
                    f = False
                    break
            if f:
                self.ans += 1
            return
        d[root.val] += 1
        self.rtl(root.left, d.copy())
        self.rtl(root.right, d.copy())
                    
    # R-to-L paths
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        d = defaultdict(int)
        self.ans = 0
        self.rtl(root, d)
        return self.ans
            
        
        
        
        