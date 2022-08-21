# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def level(self, root, ans, level):
        if root is None:
            return
        ans[level].append(root.val)
        self.level(root.left, ans, level + 1)
        self.level(root.right, ans, level + 1)
        
        
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        ans = [[] for i in range(3000)]
        self.level(root, ans, level)
        while [] in ans:
            ans.remove([])
        return ans[::-1]        
