# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Level and reverse
        if not root:
            return []
        adj = [[]]
        q = [(root, 0)]
        while q:
            root, level = q.pop(0)
            print(root.val, level)
            adj[level].append(root.val)
            adj.append([])
            if root.left:
                q.append((root.left, level + 1))                
            if root.right:
                q.append((root.right, level + 1))
        print(adj)
        ans = []
        for i in range(len(adj)):
            if adj[i]:
                if i % 2:
                    ans.append(adj[i][::-1])
                else:
                    ans.append(adj[i])
        return ans
                
            
        
        