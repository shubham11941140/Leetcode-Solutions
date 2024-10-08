# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # Start with the 'right' direction
        row, col = 0, 0  # Start from the top-left corner
        while head:
            matrix[row][col] = head.val
            head = head.next
            nr, nc = row + directions[dir_idx][0], col + directions[dir_idx][1]
            if not (0 <= nr < m and 0 <= nc < n and matrix[nr][nc] == -1):
                dir_idx = (dir_idx + 1) % 4
                nr, nc = row + directions[dir_idx][0], col + directions[dir_idx][1]
            row, col = nr, nc
        return matrix        