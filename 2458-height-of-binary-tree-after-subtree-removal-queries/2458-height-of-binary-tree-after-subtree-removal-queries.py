# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:     
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def calc(node, height):
            if not node:
                return height - 1
            leftH, rightH = calc(node.left, height + 1), calc(node.right, height+1)
            if node.left:
                treeDict[node.left.val] = rightH
            if node.right:
                treeDict[node.right.val] = leftH
            return max(leftH, rightH)

        def updateTreeDict(node, maxheight):
            if not node: 
                return 
            if maxheight == -2 or treeDict[node.val] > maxheight:
                maxheight = treeDict[node.val]
            if node.left and maxheight > treeDict[node.left.val]:
                treeDict[node.left.val] = maxheight
            if node.right and maxheight > treeDict[node.right.val]:
                treeDict[node.right.val]= maxheight
            updateTreeDict(node.left,  maxheight)
            updateTreeDict(node.right, maxheight)
        
        treeDict = defaultdict(int)
        calc(root, 0)
        updateTreeDict(root, -2)
        return [treeDict[i] for i in queries]




        