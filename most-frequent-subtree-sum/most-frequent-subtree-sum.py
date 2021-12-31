# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    
    def ssum(self, root):
        if root is None:
            return 0
        else:
            return root.val + self.ssum(root.left) + self.ssum(root.right)
    
    def all(self, root, a):
        if root is None:
            return
        else:
            a.append(self.ssum(root))
            self.all(root.left, a)
            self.all(root.right, a)    
    
            
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        a = []
        self.all(root, a)
        f = Counter(a)
        m = max(f.values())
        return [i for i in f if f[i] == m]
                
        