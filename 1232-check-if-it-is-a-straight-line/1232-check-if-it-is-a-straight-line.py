class Solution:

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        c1 = coordinates[0]
        c2 = coordinates[1]
        if c1[0] == c2[0]:
            x = c1[0]
            for i in coordinates:
                if i[0] != x:
                    return False
            return True
        m = (c2[1] - c1[1]) / (c2[0] - c1[0])
        b = c1[1] - m * c1[0]
        print(m, b)
        for i in coordinates:
            if i[1] != (m * i[0] + b):
                return False
        return True
