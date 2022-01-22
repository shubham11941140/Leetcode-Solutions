# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    # 2 DFS to solve this
    # FIND E1
    def dfs1(self, root, curmax, e1):        
        rl = self.dfs1(root.left, curmax, e1) if root.left else -5000
        rr = self.dfs1(root.right, curmax, e1) if root.right else -5000
        print("RRRL", rl, rr)
        if rl == -5000 and rr == -5000:
            cursum = root.val
        else:
            cursum = root.val + max(rl, rr)
            print("CURSUM", root.val, cursum)
        curmax = max(curmax, cursum)
        print(curmax)
        if rl > rr:
            e1 = root.left
        else:
            e1 = root.right
            #print(e1.val)
        return cursum
     
        
    def path(self, root, rooted):
        # DP BOTTOM UP ON TREES SOLUTION
        if root is None:
            return -5000
        # Compute left, right
        l = self.path(root.left, rooted)
        r = self.path(root.right, rooted)
        # IF rooted 
        # Ans is the ans
        tos = root.val
        if l < 0 and r < 0:
            tos = max(tos, root.val)
        elif l < 0:
            tos = max(tos, root.val + r)
        elif r < 0:
            tos = max(tos, root.val + l)
        else:
            tos = max(tos, root.val + l + r)
        rooted[root.val] = tos
        #val + left + root
        
        # IF NOT rooted
        if l < 0 and r < 0:
            return root.val
        else:
            return root.val + max(l, r)
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        e1 = root
        v = self.dfs1(root, -5000, e1)
        print(v, e1.val)
        '''
        rooted = [-50] * (10 ** 5)
        self.path(root, rooted)
        print(rooted[:100])
        return max(rooted)
        
        
        
        