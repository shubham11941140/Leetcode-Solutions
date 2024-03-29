class Solution:

    @staticmethod
    def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        c = 0
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i -
                                               1] == 0 and flowerbed[i +
                                                                     1] == 0:
                c += 1
                flowerbed[i] = 1
        return n <= c
