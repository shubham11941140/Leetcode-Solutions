# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, val, path):
            if not node:
                return False
            if node.val == val:
                return True
            if dfs(node.left, val, path):
                path.append('L')
            elif dfs(node.right, val, path):
                path.append('R')
            return bool(path)

        pathToStart, pathToDest = [], []
        dfs(root, startValue, pathToStart)
        dfs(root, destValue, pathToDest)

        # Remove common path elements
        while pathToStart and pathToDest and pathToStart[-1] == pathToDest[-1]:
            pathToStart.pop()
            pathToDest.pop()

        # Construct the final path
        return 'U' * len(pathToStart) + ''.join(pathToDest[::-1])        