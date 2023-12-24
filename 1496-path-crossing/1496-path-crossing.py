class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(x, y)}
        direction = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}

        for move in path:
            dx, dy = direction[move]
            x, y = x + dx, y + dy
            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False        