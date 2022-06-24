# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        l = []
        a = []
        q = [(root, 0)]
        while q:
            root, level = q.pop(0)
            l.append(level)
            a.append(root.val)
            if root.left:
                q.append((root.left, level + 1))
            if root.right:
                q.append((root.right, level + 1))
        m = max(l)
        idx = l.index(m)
        return a[idx]
        