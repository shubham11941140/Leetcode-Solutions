# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]

        # Directions for right, down, left, and up movements
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # Start with the 'right' direction

        row, col = 0, 0  # Start from the top-left corner

        while head:
            matrix[row][col] = head.val
            head = head.next

            # Calculate the next position
            next_row, next_col = row + directions[dir_idx][0], col + directions[dir_idx][1]

            # Check if the next position is within bounds and not yet filled
            if not (0 <= next_row < m and 0 <= next_col < n and matrix[next_row][next_col] == -1):
                # Change direction
                dir_idx = (dir_idx + 1) % 4
                next_row, next_col = row + directions[dir_idx][0], col + directions[dir_idx][1]

            row, col = next_row, next_col

        return matrix        