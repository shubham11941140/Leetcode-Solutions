# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def same(self, root1, root2):
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (root1 and not root2):
            return False
        if root1.val == root2.val:
            return self.same(root1.left, root2.left) and self.same(root1.right, root2.right)
        return False
    
    
    def flip(self, root1, r):
        if not root1:
            return
        #if root1 and not r:            r = TreeNode()
        #r = TreeNode()
        r.val = root1.val
        print(24, r.val)
        if root1.right and not r.left:
            r.left = TreeNode()
            self.flip(root1.right, r.left)
        if root1.left and not r.right:
            r.right = TreeNode()
            self.flip(root1.left, r.right)

    
    def tra(self, root):
        if not root:
            return
        self.tra(root.left)
        print(root.val)
        self.tra(root.right)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # Flip tree and check same
        # Recursively
        self.tra(root)
        r = TreeNode()
        print(r.val)
        self.flip(root, r)
        print(43)
        self.tra(r)
        
        return self.same(root, r)
    
        adj = [[] for i in range(2000)]
        q = []
        q.append((root, 0))
        while q:
            root, level = q.pop(0)
            if root is None:
                root = TreeNode(-200)
            adj[level].append(root.val)
            q.append((root.left, level + 1))
            q.append((root.right, level + 1))
            #print(level, adj[level])
            if adj[level - 1] != adj[level - 1][::-1]:
                return False
            if len(set(adj[level - 1])) == 1 and adj[level - 1][0] == -200:
                break
                
        for arr in adj:
            if not arr:
                break
            elif arr != arr[::-1]:
                return False
        return True
                
            

        