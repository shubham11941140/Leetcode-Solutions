from bisect import insort


class MedianFinder:

    def __init__(self):
        self.a = []
        self.l = 0

    def addNum(self, num: int) -> None:
        insort(self.a, num)
        self.l += 1
        # print(self.a)

    def findMedian(self) -> float:
        if self.l % 2:
            return self.a[self.l // 2]
        return (self.a[self.l // 2] + self.a[(self.l // 2) - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
