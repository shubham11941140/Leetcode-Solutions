class Solution:

    @staticmethod
    def minMoves(t: int, d: int) -> int:
        c = 0
        while d and t > 1:
            c += 1
            if t % 2:
                t -= 1
            else:
                t //= 2
                d -= 1
        return c if t == 1 else c + t - 1
