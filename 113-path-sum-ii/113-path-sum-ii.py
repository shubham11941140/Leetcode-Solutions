# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def roottoleafsum(self, root, a, patharr):
        patharr.append(root.val)
        if root.left is None and root.right is None:            
            a.append(patharr.copy())
        else:            
            if root.left:
                self.roottoleafsum(root.left, a, patharr)
            if root.right:
                self.roottoleafsum(root.right, a, patharr)
        patharr.pop()
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        a = []
        val = []
        self.roottoleafsum(root, a, val)    
        return [i for i in a if sum(i) == targetSum]