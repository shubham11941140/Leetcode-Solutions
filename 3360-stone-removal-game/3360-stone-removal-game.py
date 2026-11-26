class Solution:
    def canAliceWin(self, n: int) -> bool:
        unplayed = round(sqrt(2 * (55 - n)))
        return unplayed % 2 == 1