# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return Counter()
            if not node.left and not node.right:
                return Counter({1: 1})
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Count good pairs between left and right subtrees
            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.result += left[l] * right[r]
            
            # Combine left and right subtree distances
            combined = Counter()
            for d in left:
                combined[d + 1] += left[d]
            for d in right:
                combined[d + 1] += right[d]
            
            return combined
        
        self.result = 0
        dfs(root)
        return self.result        