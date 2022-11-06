class Solution:

    def carFleet(self, target: int, position: List[int],
                 speed: List[int]) -> int:
        n = len(position)
        if n == 0:
            return 0
        cars = sorted(zip(position, speed))
        ans = 1
        t = (target - cars[-1][0]) / cars[-1][1]
        for i in range(n - 2, -1, -1):
            nt = (target - cars[i][0]) / cars[i][1]
            if nt > t:
                ans += 1
                t = nt
        return ans
