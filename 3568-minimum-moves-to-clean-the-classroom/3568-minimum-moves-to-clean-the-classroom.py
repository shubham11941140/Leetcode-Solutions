class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        # Find starting position and assign indices to litter
        start = None
        litter = {}
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)
        k = len(litter)
        target = (1 << k) - 1
        # State: (row, col, mask, remaining_energy)
        q = deque([(start[0], start[1], 0, energy)])
        visited = {(start[0], start[1], 0, energy)}
        moves = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for _ in range(len(q)):
                r, c, mask, curr_energy = q.popleft()
                if mask == target:
                    return moves
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if classroom[nr][nc] == 'X':
                        continue
                    # Every move costs 1 energy
                    if curr_energy == 0:
                        continue
                    new_energy = curr_energy - 1
                    new_mask = mask
                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        idx = litter[(nr, nc)]
                        new_mask |= 1 << idx
                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        new_energy = energy
                    # If energy becomes 0, we can only continue from R.
                    # It is still okay if this move collected the final litter.
                    if new_energy == 0 and classroom[nr][nc] != 'R':
                        if new_mask != target:
                            continue
                    state = (nr, nc, new_mask, new_energy)
                    if state not in visited:
                        visited.add(state)
                        q.append(state)
            moves += 1
        return -1