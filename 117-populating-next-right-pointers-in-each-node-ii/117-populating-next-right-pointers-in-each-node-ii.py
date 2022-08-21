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

    def connect(self, root: "Node") -> "Node":
        if not root:
            return
        head = root
        adj = [[] for i in range(7000)]
        level = 0
        q = [(root, level)]
        adj[level].append(root)
        while q:
            root, level = q.pop(0)
            adj[level].append(root)
            if root.left:
                q.append((root.left, level + 1))
            if root.right:
                q.append((root.right, level + 1))
        for level in range(7000):
            if adj[level]:
                r = None
                for i in adj[level][::-1]:
                    r = self.insert(r, i)
                if level:
                    adj[level][0].val = r.val
                    adj[level][0].left = r.left
                    adj[level][0].right = r.right
                    adj[level][0].next = r.next
            else:
                break
        return head
