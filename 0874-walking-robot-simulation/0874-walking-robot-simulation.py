class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction_vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Convert obstacles to a set of tuples for faster lookup
        obstacles = set(map(tuple, obstacles))
        # Initialize the robot's starting position and direction
        x, y, direction = 0, 0, 0
        max_distance = 0
        
        for command in commands:
            if command == -2:  # Turn left
                direction = (direction - 1) % 4
            elif command == -1:  # Turn right
                direction = (direction + 1) % 4
            else:  # Move forward
                for _ in range(command):
                    next_x = x + direction_vectors[direction][0]
                    next_y = y + direction_vectors[direction][1]
                    if (next_x, next_y) not in obstacles:
                        x, y = next_x, next_y
                        max_distance = max(max_distance, x*x + y*y)
                    else:
                        break
        
        return max_distance        