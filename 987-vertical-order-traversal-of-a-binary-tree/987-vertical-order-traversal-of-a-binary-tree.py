# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [(root, 0, 0)]
        a = [[] for i in range(2500)]
        while q:
            root, row, col = q.pop(0)
            a[col + 1100].append((row, root.val))
            if root.left:
                q.append((root.left, row + 1, col - 1))
            if root.right:
                q.append((root.right, row + 1, col + 1))
        b = [sorted(i) for i in a if i]
        return [[j[1] for j in i] for i in b]
            
        