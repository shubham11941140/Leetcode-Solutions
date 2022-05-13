"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:

    def insert(self, root, item):
        temp = Node(0)
        temp.val = item.val
        temp.left = item.left
        temp.right = item.right
        temp.next = root
        root = temp
        return root        
    
    
    
    def connect(self, root: 'Node') -> 'Node':
        # LOT
        q = []
        head = root
        if not root:
            return
        adj = [[] for i in range(7000)]
        level = 0
        q.append((root, level))
        adj[level].append(root)
        while q:
            root, level = q.pop(0)
            adj[level].append(root)
            if root.left:
                q.append((root.left, level + 1))
            if root.right:
                q.append((root.right, level + 1))
        # Convert it to linked list
        #print(adj)
        for level in range(7000):
            print(level)
            if not adj[level]:
                break
            l = len(adj[level])
            curnode = None
            #print(47, curnode.val, curnode.next)
            for i in reversed(range(l)):
                #print(49, i, adj[level][i].val, adj[level][i].next)  
                curnode = self.insert(curnode, adj[level][i])
                #adj[level][i].next = curnode
                #curnode = adj[level][i]
                print(52, curnode.val, curnode.next)
            print("HOORAH")
            if level:
                adj[level][0].val = curnode.val
                adj[level][0].left = curnode.left
                adj[level][0].right = curnode.right
                adj[level][0].next = curnode.next
        return head
    
        print("54")
        
        
        
        
        r = None
        for level in range(7000):
            print(level)
            if not adj[level]:
                break
            else:
                # A proper nodes exist
                #r = None
                for i in adj[level][::-1]:
                    r = self.insert(r, i)  
                y = r
                while y is not None:
                    print(52, y.val)
                    
                    y = y.next
        return head
        