class Solution:

    def countTriples(self, n: int) -> int:
        cnt = 0
        # Iterate a from 1 to n
        for a in range(1, n):
            # Iterate b from a + 1 to n
            for b in range(a + 1, n):
                # Check if c is a perfect square and within range
                if (int((a * a + b * b)**0.5)**2 == (a * a + b * b) and int(
                        (a * a + b * b)**0.5) <= n):
                    cnt += 2  # Count both (a, b, c) and (b, a, c)
        return cnt
