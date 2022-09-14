# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

class Solution:            
    
    def rtl(self, root, d):
        if not root:
            return
        if not root.left and not root.right:
            d[root.val] += 1
            self.ans.append(d.copy())
            return
        d[root.val] += 1
        self.rtl(root.left, d.copy())
        self.rtl(root.right, d.copy())
        #d[root.val] -= 1
        
    def ps(self, a):
        z = 0
        for i in a.values():
            if i % 2 == 1:
                z += 1
            if z > 1:
                return False
        return True
                    
    # R-to-L paths
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        a = []
        d = defaultdict(int)
        self.ans = []
        self.rtl(root, d)
        print(self.ans)
        r = 0
        for i in self.ans:
            if self.ps(i):
                r += 1
        return r
            
        
        
        
        