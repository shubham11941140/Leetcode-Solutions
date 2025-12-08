class Solution:
    def countTriples(self, n: int) -> int:
        c = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for k in range(1, n + 1):
                    if i ** 2 == j ** 2 + k ** 2:
                        c += 1
        return c
        