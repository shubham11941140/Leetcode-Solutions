# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = [(root, 0)]
        adj = [[] for i in range(200)]
        while q:
            root, level = q.pop(0)
            adj[level].append(root.val)
            if root.left:
                q.append((root.left, level + 1))
            if root.right:
                q.append((root.right, level + 1))
        return [i[-1] for i in adj if i]
