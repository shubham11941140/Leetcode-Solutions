class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        R, C = len(grid), len(grid[0])
        def ak(keys, k):
            return keys | (1 << (ord(k) - ord('a')))
        def hk(keys, k):
            return (keys & (1 << (ord(k) - ord('a')))) != 0
        dist = [[[float('inf')] * 64 for _ in range(C)] for _ in range(R)]
        queue = []
        targetKeys = 0
        for r in range(R):
            for c in range(C):
                ch = grid[r][c]
                if ch == '@':
                    queue.append((r, c, 0, 0))
                    dist[r][c][0] = 0
                elif ch.islower():
                    targetKeys = ak(targetKeys, ch)
        while queue:
            r, c, step, keys = queue.pop(0)
            if keys == targetKeys:
                return step
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < R and 0 <= nc < C) or grid[nr][nc] == '#':
                    continue
                if grid[nr][nc].isupper() and not hk(keys, grid[nr][nc].lower()):
                    continue
                nk = ak(keys, grid[nr][nc]) if grid[nr][nc].islower() else keys
                if step + 1 < dist[nr][nc][nk]:
                    dist[nr][nc][nk] = step + 1
                    queue.append((nr, nc, step + 1, nk))
        return -1        