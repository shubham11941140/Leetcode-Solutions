class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        c = 0
        for i in range(1, len(flowerbed) - 1):
            if not flowerbed[i] and not flowerbed[i - 1] and not flowerbed[i + 1]:
                c += 1
                flowerbed[i] = 1
        return n <= c
