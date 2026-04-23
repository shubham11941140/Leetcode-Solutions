class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        self.n = len(board)
        visited = set()
        queue = deque()
        queue.append((1, 0))
        visited.add(1)
        while queue:
            node, steps = queue.popleft()
            if node == self.n**2:
                return steps
            for i in range(node + 1, node + 7):
                if i > self.n**2:
                    break
                x, y = self.get_coordinates(i)
                if board[x][y] != -1:
                    i = board[x][y]
                if i not in visited:
                    queue.append((i, steps + 1))
                    visited.add(i)
        return -1

    def get_coordinates(self, i):
        quot, rem = divmod(i - 1, self.n)
        row = self.n - 1 - quot
        col = rem if row % 2 != self.n % 2 else self.n - 1 - rem
        return row, col
