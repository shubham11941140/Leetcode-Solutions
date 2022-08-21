class Solution:

    @staticmethod
    def countPoints(points: List[List[int]],
                    queries: List[List[int]]) -> List[int]:
        ans = []
        for x, y, r in queries:
            c = 0
            for i, j in points:
                if (x - i)**2 + (y - j)**2 <= r**2:
                    c += 1
            print(c)
            ans.append(c)
        return ans
