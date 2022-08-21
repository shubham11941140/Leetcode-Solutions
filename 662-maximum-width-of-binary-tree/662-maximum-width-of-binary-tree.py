# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def widthOfBinaryTree(root: Optional[TreeNode]) -> int:
        a = [[] for i in range(4000)]
        q = [(root, 0, 0)]
        while q:
            r, l, idx = q.pop(0)
            a[l].append(idx)
            if r.left:
                q.append((r.left, l + 1, 2 * idx))
            if r.right:
                q.append((r.right, l + 1, 2 * idx + 1))
        return max([max(i) - min(i) + 1 for i in a if i])
