class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join(str(num) for row in board for num in row)
        target = '123450'
        # Define the neighbors for each position in the 2x3 board
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        # Initialize the queue for BFS
        queue = deque([(start, start.index('0'), 0)])
        visited = set()
        visited.add(start)
        while queue:
            state, z, steps = queue.popleft()
            # Check if we have reached the target state
            if state == target:
                return steps
            # Explore all possible moves
            for neighbor in neighbors[z]:
                new_state = list(state)
                new_state[z], new_state[neighbor] = new_state[neighbor], new_state[z]
                new_state = ''.join(new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, neighbor, steps + 1))
        return -1        