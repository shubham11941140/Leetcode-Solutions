# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def largestValues(root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        a = [[] for i in range(10**5)]
        q = [(root, 0)]
        while q:
            r, level = q.pop(0)
            a[level].append(r.val)
            if r.left:
                q.append((r.left, level + 1))
            if r.right:
                q.append((r.right, level + 1))
        return [max(i) for i in a if i]
