class Solution:
    def isRobotBounded(self, instructions: str) -> bool:        
        d = instructions * 15        
        ad = ["N", "E", "S", "W"]
        didx = 0
        direction = ad[didx]
        path = [(0, 0)]
        x = 0
        y = 0
        for i in range(len(d)):
            if d[i] == "G":
                # Go 1 unit in that particualr iidrectons
                if direction == "N":
                    y += 1
                elif direction == "S":
                    y -= 1
                elif direction == "E":
                    x += 1
                elif direction == "W":
                    x -= 1
                if (x, y) not in path:
                    path.append((x, y))
            elif d[i] == "L":
                didx = (didx + 3) % 4
            elif d[i] == "R":
                didx = (didx + 1) % 4
            direction = ad[didx]        
        j = path.copy()
        d = instructions
        for i in range(len(d)):
            if d[i] == "G":
                if direction == "N":
                    y += 1
                elif direction == "S":
                    y -= 1
                elif direction == "E":
                    x += 1
                elif direction == "W":
                    x -= 1
                if (x, y) not in path:
                    path.append((x, y))
            elif d[i] == "L":
                didx = (didx + 3) % 4
            elif d[i] == "R":
                didx = (didx + 1) % 4
            direction = ad[didx]              
        return j == path
        