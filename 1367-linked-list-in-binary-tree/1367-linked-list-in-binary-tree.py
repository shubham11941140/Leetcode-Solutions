# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:            
        
    def subPathCheck(self, node, llHead):
        curr = llHead
        q2 = [[node, curr]]        
        while len(q2):
            newNode, llNode = q2.pop(0)
            if newNode.val == llNode.val:
                if llNode.next == None:
                    return True
                if newNode.left != None and llNode.next != None:
                    q2.append([newNode.left, llNode.next])
                if newNode.right != None and llNode.next != None:
                    q2.append([newNode.right, llNode.next])
        return False
    
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        q = [root]
        while len(q):
            tempNode = q.pop(0)
            if tempNode != None:
                if tempNode.val == head.val:
                    if self.subPathCheck(tempNode, head):
                        return True
                if tempNode.left != None:
                    q.append(tempNode.left)
                if tempNode.right != None:
                    q.append(tempNode.right)
        return False

        