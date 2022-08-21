# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def roottoleafsum(self, root, a, val):
        if not val:
            val += str(root.val)
        else:
            val += "->" + str(root.val)
        if root.left is None and root.right is None:
            a.append(val)
        else:            
            if root.left:
                self.roottoleafsum(root.left, a, val)
            if root.right:
                self.roottoleafsum(root.right, a, val)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        a = []
        val = ""
        self.roottoleafsum(root, a, val)
        return a        
