class Robot:
    def __init__(self, index, position, health, direction):
        self.i = index
        self.p = position
        self.h = health
        self.d = direction

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        ans = []
        stack = []  # The running robots
        robots = sorted([Robot(i, positions[i], healths[i], directions[i]) for i in range(len(positions))], key = lambda x: x.p)        
        for robot in robots:
            if robot.d == 'R':
                stack.append(robot)
                continue
            # Collide with robots going right
            while stack and stack[-1].d == 'R' and robot.h > 0:
                if stack[-1].h == robot.h:
                    stack.pop()
                    robot.h = 0
                elif stack[-1].h < robot.h:
                    stack.pop()
                    robot.h -= 1
                else:
                    stack[-1].h -= 1
                    robot.h = 0
            if robot.h > 0:
                stack.append(robot)
        return ans + [robot.h for robot in sorted(stack, key = lambda x: x.i)] 