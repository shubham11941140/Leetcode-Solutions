# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    
    def __init__(self):
        self.ans = None
    
    def find(self, root, item):
        if root.val == item:
            #print(item) 
            self.ans = root
            return root
        if root.left:
            self.find(root.left, item)
        if root.right:
            self.find(root.right, item)
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        t = target.val
        #print(t)
        if cloned:
            ans = self.find(cloned, t)
            print("ANS", ans, self.ans)
            return self.ans
        return None
        