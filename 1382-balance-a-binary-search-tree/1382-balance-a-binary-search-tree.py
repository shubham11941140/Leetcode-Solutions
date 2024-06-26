# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def storeBSTNodes(self, root, nodes):
        if root:
            self.storeBSTNodes(root.left, nodes)
            nodes.append(root)
            self.storeBSTNodes(root.right, nodes)

    def buildTreeUtil(self, nodes, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = nodes[mid]
        root.left = self.buildTreeUtil(nodes, start, mid - 1)
        root.right = self.buildTreeUtil(nodes, mid + 1, end)
        return root    
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        self.storeBSTNodes(root, nodes)
        n = len(nodes)
        return self.buildTreeUtil(nodes, 0, n - 1)        
        