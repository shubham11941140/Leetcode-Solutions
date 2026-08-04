class Solution:

    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left_operations = [0] * n
        right_operations = [0] * n
        # Calculate the operations from the left
        count = int(boxes[0])
        for i in range(1, n):
            left_operations[i] = left_operations[i - 1] + count
            count += int(boxes[i])
        # Calculate the operations from the right
        count = int(boxes[n - 1])
        for i in range(n - 2, -1, -1):
            right_operations[i] = right_operations[i + 1] + count
            count += int(boxes[i])
        # Combine the operations
        return [left_operations[i] + right_operations[i] for i in range(n)]
