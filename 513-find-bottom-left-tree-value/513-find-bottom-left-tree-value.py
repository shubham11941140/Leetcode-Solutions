# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # BFS
        adj = [[] for i in range(10 ** 4 + 100)]
        q = [(root, 0)]
        while q:
            root, level = q.pop(0)
            adj[level].append(root)
            if root.left:
                q.append((root.left, level + 1))
            if root.right:
                q.append((root.right, level + 1))
                
        
        while [] in adj:
            adj.remove([])
        #print(adj)
        #print(adj[-1])
        for i in adj[-1]:
            return i.val
        