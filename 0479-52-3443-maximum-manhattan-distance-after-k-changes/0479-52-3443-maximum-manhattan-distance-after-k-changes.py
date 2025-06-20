class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def simulate(primary: str, secondary: str) -> int:
            dist = 0
            max_dist = 0
            changes = 0

            for ch in s:
                if ch == primary or ch == secondary:
                    dist += 1
                elif changes < k:
                    changes += 1
                    dist += 1
                else:
                    dist -= 1  # can't change, and it's not helpful
                max_dist = max(max_dist, dist)
            return max_dist

        directions = [('N', 'E'), ('N', 'W'), ('S', 'E'), ('S', 'W')]
        return max(simulate(a, b) for a, b in directions)        