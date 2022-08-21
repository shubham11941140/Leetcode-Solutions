"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:

    @staticmethod
    def copyRandomList(head: "Optional[Node]") -> "Optional[Node]":
        first = head
        mappair = {None: None}
        new = Node(0)
        copy = new
        while first:
            new.next = Node(first.val)
            mappair[first] = new.next
            new = new.next
            first = first.next
        first = head
        while first:
            mappair[first].random = mappair[first.random]
            first = first.next
        return copy.next
