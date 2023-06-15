# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        a = [[] for i in range(10000)]
        q = [(root, 1)]
        while q:
            root, l = q.pop(0)
            a[l].append(root.val)
            if root.left:
                q.append((root.left, l + 1))
            if root.right:
                q.append((root.right, l + 1))
        #print(a)
        b = [sum(i) for i in a if i]
        return b.index(max(b)) + 1
                
        
        