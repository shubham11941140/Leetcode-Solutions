class Solution:
    def canAliceWin(self, n: int) -> bool:
        return round(sqrt(2 * (55 - n))) % 2 == 1