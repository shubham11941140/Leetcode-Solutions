# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        current = head
        while current and current.next:
            # Calculate the GCD of current node and next node
            gcd_value = gcd(current.val, current.next.val)
            # Create a new node with the GCD value
            new_node = ListNode(gcd_value)
            # Insert the new node between current and next node
            new_node.next = current.next
            current.next = new_node
            # Move to the next pair of nodes
            current = new_node.next
        return head
