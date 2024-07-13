class Robot:
    def __init__(self, index, position, health, direction):
        self.index = index
        self.position = position
        self.health = health
        self.direction = direction

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        ans = []
        robots = []
        stack = []  # The running robots

        # Create Robot objects
        for i in range(len(positions)):
            robots.append(Robot(i, positions[i], healths[i], directions[i]))

        # Sort robots by position
        robots.sort(key=lambda x: x.position)

        for robot in robots:
            if robot.direction == 'R':
                stack.append(robot)
                continue

            # Collide with robots going right
            while stack and stack[-1].direction == 'R' and robot.health > 0:
                if stack[-1].health == robot.health:
                    stack.pop()
                    robot.health = 0
                elif stack[-1].health < robot.health:
                    stack.pop()
                    robot.health -= 1
                else:
                    stack[-1].health -= 1
                    robot.health = 0

            if robot.health > 0:
                stack.append(robot)

        # Sort stack by original index
        stack.sort(key=lambda x: x.index)

        for robot in stack:
            ans.append(robot.health)

        return ans        