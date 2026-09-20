class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        return (max(x1, min(x2, xCenter)) - xCenter) ** 2 + (max(y1, min(y2, yCenter)) - yCenter) ** 2 <= radius ** 2